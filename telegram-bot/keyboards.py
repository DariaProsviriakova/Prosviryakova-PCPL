from aiogram import types
from config import VOCABULARY_BY_TOPIC

def get_main_keyboard():
    return types.ReplyKeyboardMarkup(
        keyboard=[
            [types.KeyboardButton(text="Теория"), types.KeyboardButton(text="Практика")],
            [types.KeyboardButton(text="Фразы дня"), types.KeyboardButton(text="Главное меню")]
        ],
        resize_keyboard=True
    )

def get_theory_keyboard():
    return types.ReplyKeyboardMarkup(
        keyboard=[
            [types.KeyboardButton(text="Новые слова"), types.KeyboardButton(text="Грамматика")],
            [types.KeyboardButton(text="Сменить тему"), types.KeyboardButton(text="Главное меню")]
        ],
        resize_keyboard=True
    )

def get_topics_keyboard():
    topics = list(VOCABULARY_BY_TOPIC.keys())
    keyboard = []
    
    for i in range(0, len(topics), 2):
        row = topics[i:i+2]
        keyboard.append([types.KeyboardButton(text=topic) for topic in row])
    
    keyboard.append([types.KeyboardButton(text="К теории")])
    
    return types.ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)

def get_exercise_keyboard(options):
    buttons = []
    row = []
    
    for option in options:
        row.append(types.KeyboardButton(text=option))
        if len(row) == 2:
            buttons.append(row)
            row = []
    
    if row:
        buttons.append(row)
    
    buttons.append([types.KeyboardButton(text="Назад к практике")])
    
    return types.ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)

def get_exercise_feedback_keyboard():
    return types.ReplyKeyboardMarkup(
        keyboard=[
            [types.KeyboardButton(text="Следующий вопрос"), types.KeyboardButton(text="Назад к практике")]
        ],
        resize_keyboard=True
    )

def get_grammar_keyboard():
    return types.ReplyKeyboardMarkup(
        keyboard=[
            [types.KeyboardButton(text="Present Simple"), types.KeyboardButton(text="Past Simple")],
            [types.KeyboardButton(text="Future Simple"), types.KeyboardButton(text="Present Continuous")],
            [types.KeyboardButton(text="Артикли"), types.KeyboardButton(text="Предлоги")],
            [types.KeyboardButton(text="Модальные глаголы"), types.KeyboardButton(text="К теории")]
        ],
        resize_keyboard=True
    )