import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
import random

from config import *
from database import *
from keyboards import *

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(storage=MemoryStorage())

class TheoryStates(StatesGroup):
    THEORY = State()

class PracticeStates(StatesGroup):
    PRACTICE = State()
    WAITING_FOR_ANSWER = State()

@dp.message(Command("cancel"))
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    
    await state.clear()
    await message.answer(
        "Действие отменено. Возвращаю в главное меню.",
        reply_markup=get_main_keyboard()
    )

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    user_id = message.from_user.id
    init_user_data(user_id)
    
    welcome_message = (
        f"*Добро пожаловать в языковой бот!*\n\n"
        f"Я помогу вам изучать английский язык эффективно.\n\n"
        f"*Доступные режимы:*\n"
        f"• Теория - изучение новых слов и грамматики\n"
        f"• Практика - упражнения для закрепления\n"
        f"• Фразы дня - полезные выражения\n\n"
        f"Выберите режим:"
    )
    
    await message.answer(
        welcome_message,
        reply_markup=get_main_keyboard(),
        parse_mode="Markdown"
    )

@dp.message(F.text == "Главное меню")
async def main_menu(message: types.Message, state: FSMContext):
    await state.clear()
    await cmd_start(message)

@dp.message(F.text == "Фразы дня")
async def show_phrases_of_day(message: types.Message):
    phrases = get_daily_phrases()
    
    response = "*Фразы дня:*\n\n"
    for i, phrase in enumerate(phrases, 1):
        response += f"{i}. *{phrase['en']}*\n"
        response += f"   Перевод: {phrase['ru']}\n"
        response += f"   Контекст: {phrase['context']}\n\n"
        
    await message.answer(
        response,
        reply_markup=types.ReplyKeyboardMarkup(
            keyboard=[
                [types.KeyboardButton(text="Новые фразы")],
                [types.KeyboardButton(text="Главное меню")]
            ],
            resize_keyboard=True
        ),
        parse_mode="Markdown"
    )

@dp.message(F.text == "Новые фразы")
async def get_new_phrases(message: types.Message):
    phrases = get_daily_phrases()
    
    response = "*Новые фразы дня:*\n\n"
    for i, phrase in enumerate(phrases, 1):
        response += f"{i}. *{phrase['en']}*\n"
        response += f"   Перевод: {phrase['ru']}\n"
        response += f"   Контекст: {phrase['context']}\n\n"
        
    await message.answer(
        response,
        reply_markup=types.ReplyKeyboardMarkup(
            keyboard=[
                [types.KeyboardButton(text="Еще фразы")],
                [types.KeyboardButton(text="Главное меню")]
            ],
            resize_keyboard=True
        ),
        parse_mode="Markdown"
    )

@dp.message(F.text == "Еще фразы")
async def get_more_phrases(message: types.Message):
    await get_new_phrases(message)

@dp.message(F.text == "Теория")
async def start_theory(message: types.Message, state: FSMContext):
    await state.set_state(TheoryStates.THEORY)
    user_id = message.from_user.id
    settings = get_user_settings(user_id)
    topic = settings.get("current_topic", "Еда")
    
    await message.answer(
        f"*Режим теории*\n\nТекущая тема: *{topic}*\nВыберите тип материала:",
        reply_markup=get_theory_keyboard(),
        parse_mode="Markdown"
    )

@dp.message(TheoryStates.THEORY, F.text == "Новые слова")
async def show_new_words(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    settings = get_user_settings(user_id)
    topic = settings.get("current_topic", "Еда")
    vocabulary = VOCABULARY_BY_TOPIC.get(topic, {})
    
    if vocabulary:
        response = f"*Новые слова по теме '{topic}':*\n\n"
        word_items = list(vocabulary.items())
        selected_words = random.sample(word_items, min(5, len(word_items)))
        
        for i, (en_word, data) in enumerate(selected_words, 1):
            ru_word = data["ru"]
            example = random.choice(data.get("examples", [""]))
            response += f"{i}. *{en_word}* - {ru_word}\n"
            response += f"   Пример: _{example}_\n\n"
            
            add_word_to_vocabulary(user_id, {
                "word": en_word,
                "translation": ru_word,
                "learned": False,
                "review_count": 0,
                "topic": topic
            })
        
        keyboard = types.ReplyKeyboardMarkup(
            keyboard=[
                [types.KeyboardButton(text="Запомнил слова")],
                [types.KeyboardButton(text="К теории")]
            ],
            resize_keyboard=True
        )
        response += "Нажмите 'Запомнил слова', когда будете готовы к практике!"
    else:
        response = "Для этой темы пока нет слов."
        keyboard = types.ReplyKeyboardMarkup(
            keyboard=[[types.KeyboardButton(text="К теории")]],
            resize_keyboard=True
        )
    
    await message.answer(response, reply_markup=keyboard, parse_mode="Markdown")

@dp.message(TheoryStates.THEORY, F.text == "Сменить тему")
async def change_topic(message: types.Message):
    await message.answer(
        "*Выберите тему для изучения:*\n\nКаждая тема содержит новые слова с примерами.",
        reply_markup=get_topics_keyboard(),
        parse_mode="Markdown"
    )

@dp.message(TheoryStates.THEORY, F.text.in_(list(VOCABULARY_BY_TOPIC.keys())))
async def handle_topic_selection(message: types.Message):
    user_id = message.from_user.id
    selected_topic = message.text
    
    update_user_settings(user_id, "current_topic", selected_topic)
    
    await message.answer(
        f"Тема изменена на: *{selected_topic}*\n\n"
        f"Теперь вы можете изучать новые слова по этой теме.",
        parse_mode="Markdown",
        reply_markup=get_theory_keyboard()
    )

@dp.message(TheoryStates.THEORY, F.text == "Грамматика")
async def show_grammar(message: types.Message):
    await message.answer(
        "*Выберите тему грамматики:*\n\n"
        "Изучите правила, примеры и выполните упражнения для закрепления.\n\n"
        "*Доступные темы:*\n"
        "• Present Simple - настоящее простое\n"
        "• Past Simple - прошедшее простое\n"
        "• Future Simple - будущее простое\n"
        "• Present Continuous - настоящее продолженное\n"
        "• Артикли - a/an/the\n"
        "• Предлоги - in/on/at\n"
        "• Модальные глаголы - can/must/should",
        reply_markup=get_grammar_keyboard(),
        parse_mode="Markdown"
    )

@dp.message(F.text == "Практика")
async def start_practice(message: types.Message, state: FSMContext):
    await state.set_state(PracticeStates.PRACTICE)
    user_id = message.from_user.id
    init_user_data(user_id)
    
    vocabulary = get_user_vocabulary(user_id)
    stats = get_user_stats(user_id)
    
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=[
            [types.KeyboardButton(text="Слова: перевод"), types.KeyboardButton(text="Слова: выбор")],
            [types.KeyboardButton(text="Главное меню")]
        ],
        resize_keyboard=True
    )
    
    await message.answer(
        f"*Режим практики*\n\n*Ваша статистика:*\n"
        f"Слов в словаре: *{len(vocabulary)}*\n"
        f"Выучено слов: *{stats.get('learned_words', 0)}*\n"
        f"Точность: *{stats.get('accuracy', 0)}%*\n"
        f"Серия правильных ответов: *{stats.get('current_streak', 0)}*\n\n"
        f"Выберите тип упражнения:",
        reply_markup=keyboard,
        parse_mode="Markdown"
    )

@dp.message(PracticeStates.PRACTICE, F.text == "Слова: перевод")
async def practice_translation(message: types.Message, state: FSMContext):
    await send_word_exercise(message.from_user.id, message, state, "translation")

@dp.message(PracticeStates.PRACTICE, F.text == "Слова: выбор")
async def practice_choose_translation(message: types.Message, state: FSMContext):
    await send_word_exercise(message.from_user.id, message, state, "choose_translation")

async def send_word_exercise(user_id: int, message: types.Message, state: FSMContext, exercise_type: str = "translation"):
    vocabulary = get_user_vocabulary(user_id)
    
    if not vocabulary:
        await message.answer(
            "Нет слов для практики.\n\nСначала изучите слова в режиме Теория!",
            reply_markup=types.ReplyKeyboardMarkup(
                keyboard=[[types.KeyboardButton(text="Теория")]],
                resize_keyboard=True
            )
        )
        return
    
    word_data = get_random_word(user_id)
    if not word_data:
        await message.answer(
            "Не удалось получить слово для упражнения.",
            reply_markup=types.ReplyKeyboardMarkup(
                keyboard=[[types.KeyboardButton(text="Назад к практике")]],
                resize_keyboard=True
            )
        )
        return
    
    if exercise_type == "translation":
        word = word_data["word"]
        correct_answer = word_data["translation"]
        all_options = [w["translation"] for w in vocabulary if w["translation"] != correct_answer]
        question = f"*Переведите слово:*\n\n**{word}**\n\nВыберите правильный перевод:"
    else:
        translation = word_data["translation"]
        correct_answer = word_data["word"]
        all_options = [w["word"] for w in vocabulary if w["word"] != correct_answer]
        question = f"*Выберите слово для перевода:*\n\n**{translation}**\n\nВыберите правильное английское слово:"
    
    if len(all_options) >= 3:
        wrong_options = random.sample(all_options, 3)
    else:
        fake_options = ["стол", "окно", "дверь"] if exercise_type == "translation" else ["table", "window", "door"]
        wrong_options = random.sample([o for o in fake_options if o != correct_answer], 3)
    
    options = [correct_answer] + wrong_options
    random.shuffle(options)
    
    await state.update_data(
        correct_answer=correct_answer,
        exercise_type=exercise_type,
        word_data=word_data
    )
    
    if exercise_type == "choose_translation":
        await state.update_data(translation=translation)
    else:
        await state.update_data(word=word_data["word"])
    
    await message.answer(
        question,
        reply_markup=get_exercise_keyboard(options),
        parse_mode="Markdown"
    )
    await state.set_state(PracticeStates.WAITING_FOR_ANSWER)

@dp.message(F.text == "Следующий вопрос")
async def handle_next_question(message: types.Message, state: FSMContext):
    await state.set_state(PracticeStates.PRACTICE)
    exercises = [practice_translation, practice_choose_translation]
    await random.choice(exercises)(message, state)

@dp.message(PracticeStates.WAITING_FOR_ANSWER)
async def handle_practice_answer(message: types.Message, state: FSMContext):
    user_answer = message.text
    data = await state.get_data()
    correct_answer = data.get("correct_answer", "")
    
    is_correct = user_answer == correct_answer
    update_accuracy(message.from_user.id, is_correct)
    
    if is_correct:
        if "word_data" in data:
            word = data["word_data"]["word"]
            increment_word_review(message.from_user.id, word)
    
    if is_correct:
        prefix = "*Правильно!*"
    else:
        prefix = "*Неправильно!*"
    
    if data.get("exercise_type") == "translation":
        word = data.get("word", "")
        correct = data.get("correct_answer", "")
        if is_correct:
            response = f"{prefix}\n\n**{word}** → **{correct}**"
        else:
            response = f"{prefix}\n\n**{word}** → **{correct}**\n\nВаш ответ: {user_answer}"
    else:
        translation = data.get("translation", "")
        correct = data.get("correct_answer", "")
        if is_correct:
            response = f"{prefix}\n\n**{translation}** → **{correct}**"
        else:
            response = f"{prefix}\n\n**{translation}** → **{correct}**\n\nВаш ответ: {user_answer}"
    
    if "word_data" in data and "examples" in data["word_data"]:
        examples = data["word_data"]["examples"][:2]
        if examples:
            response += f"\n\n*Примеры использования:*"
            for example in examples:
                response += f"\n• {example}"
    
    stats = get_user_stats(message.from_user.id)
    response += f"\n\n*Статистика:*\n"
    response += f"Упражнений выполнено: *{stats.get('exercises_completed', 0)}*\n"
    response += f"Серия: *{stats.get('current_streak', 0)}*\n"
    response += f"Выучено слов: *{stats.get('learned_words', 0)}*\n"
    response += f"Точность: *{stats.get('accuracy', 0)}%*"
    
    await message.answer(
        response,
        reply_markup=get_exercise_feedback_keyboard(),
        parse_mode="Markdown"
    )
    await state.clear()

@dp.message(F.text == "К теории")
async def back_to_theory(message: types.Message, state: FSMContext):
    await state.set_state(TheoryStates.THEORY)
    await start_theory(message, state)

@dp.message(F.text == "Запомнил слова")
async def words_learned(message: types.Message):
    user_id = message.from_user.id
    progress = get_user_progress(user_id)
    vocabulary = get_user_vocabulary(user_id)
    learned_count = len([w for w in vocabulary if w.get("learned", False)])
    update_user_progress(user_id, "words_learned", learned_count)
    
    await message.answer(
        f"*Отлично!* Вы запомнили новые слова!\n\nТеперь переходите в режим Практика!",
        reply_markup=types.ReplyKeyboardMarkup(
            keyboard=[
                [types.KeyboardButton(text="Практика"), types.KeyboardButton(text="Теория")]
            ],
            resize_keyboard=True
        ),
        parse_mode="Markdown"
    )

@dp.message(F.text.contains("Назад к практике"))
async def back_to_practice_handler(message: types.Message, state: FSMContext):
    await state.set_state(PracticeStates.PRACTICE)
    await start_practice(message, state)

@dp.message(F.text.in_(list(GRAMMAR_LESSONS.keys())))
async def handle_grammar_topic(message: types.Message):
    topic = message.text
    lesson = GRAMMAR_LESSONS.get(topic)
    
    if not lesson:
        await message.answer("Эта тема грамматики еще не добавлена.")
        return
    
    response = f"{lesson['name']}\n\n"
    response += f"*{lesson['description']}*\n\n"
    
    response += "*Правила:*\n"
    for rule in lesson["rules"]:
        response += f"{rule}\n"
    
    response += "\n*Примеры:*\n"
    for example in lesson["examples"]:
        response += f"• {example}\n"
    
    if "usage" in lesson:
        response += "\n*Использование:*\n"
        for usage in lesson["usage"]:
            response += f"• {usage}\n"
    
    if "time_markers" in lesson:
        response += "\n*Маркеры времени:*\n"
        for marker in lesson["time_markers"]:
            response += f"• {marker}\n"
    
    if "exceptions" in lesson:
        response += "\n*Исключения:*\n"
        for exception in lesson["exceptions"]:
            response += f"• {exception}\n"
    
    if "features" in lesson:
        response += "\n*Особенности:*\n"
        for feature in lesson["features"]:
            response += f"• {feature}\n"
    
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=[
            [types.KeyboardButton(text="Другая тема"), types.KeyboardButton(text="К теории")]
        ],
        resize_keyboard=True
    )
    
    await message.answer(response, reply_markup=keyboard, parse_mode="Markdown")

@dp.message(F.text == "Другая тема")
async def another_grammar_topic(message: types.Message):
    await show_grammar(message)

@dp.message()
async def debug_handler(message: types.Message):
    print(f" Получено: '{message.text}'")
    print(f" Содержит 'Назад'? {'Назад' in message.text}")
    print(f" Содержит 'Назад к практике'? {'Назад к практике' in message.text}")

async def main():
    print("Бот запускается")
    print(f"Бот готов к работе")
    print(f"Основные режимы: Теория, Практика, Фразы дня")
    print(f"Команды: /start, /cancel")
    print(f"Начните с команды /start")
    print()
    
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())