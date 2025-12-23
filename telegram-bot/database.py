import random
from datetime import datetime
from config import VOCABULARY_BY_TOPIC

user_vocabulary = {}
user_progress = {}
user_settings = {}

def init_user_data(user_id: int) -> bool:

    if user_id not in user_vocabulary:
        user_vocabulary[user_id] = []
        user_progress[user_id] = {
            "words_learned": 0,
            "exercises_completed": 0,
            "current_streak": 0,
            "accuracy": 0.0,
            "total_attempts": 0,
            "correct_attempts": 0,
            "last_active": datetime.now().isoformat()
        }
        user_settings[user_id] = {
            "current_topic": " Еда",
            "daily_goal": 5,
            "difficulty": "средняя"
        }
        
        basic_words = [
            {"word": "hello", "translation": "привет", "learned": False, "review_count": 0, "topic": "Базовые"},
            {"word": "goodbye", "translation": "до свидания", "learned": False, "review_count": 0, "topic": "Базовые"},
            {"word": "please", "translation": "пожалуйста", "learned": False, "review_count": 0, "topic": "Базовые"},
            {"word": "thank you", "translation": "спасибо", "learned": False, "review_count": 0, "topic": "Базовые"},
            {"word": "sorry", "translation": "извините", "learned": False, "review_count": 0, "topic": "Базовые"},
        ]
        user_vocabulary[user_id].extend(basic_words)
    return True

def get_user_vocabulary(user_id: int):
    return user_vocabulary.get(user_id, [])

def get_user_settings(user_id: int):
    return user_settings.get(user_id, {})

def get_user_progress(user_id: int):
    return user_progress.get(user_id, {})

def get_user_stats(user_id: int):
    vocabulary = get_user_vocabulary(user_id)
    progress = get_user_progress(user_id)
    
    total_words = len(vocabulary)
    learned_words = sum(1 for w in vocabulary if w.get("learned", False))
    
    return {
        "total_words": total_words,
        "learned_words": learned_words,
        "exercises_completed": progress.get("exercises_completed", 0),
        "current_streak": progress.get("current_streak", 0),
        "accuracy": progress.get("accuracy", 0.0)
    }

def update_user_progress(user_id: int, key: str, value):
    if user_id in user_progress:
        user_progress[user_id][key] = value
        return True
    return False

def update_user_settings(user_id: int, key: str, value):
    if user_id in user_settings:
        user_settings[user_id][key] = value
        return True
    return False

def add_word_to_vocabulary(user_id: int, word_data: dict):
    if user_id not in user_vocabulary:
        user_vocabulary[user_id] = []
    
    existing_words = [w.get("word") for w in user_vocabulary[user_id]]
    if word_data.get("word") not in existing_words:
        user_vocabulary[user_id].append(word_data)
        return True
    return False

def get_random_word(user_id: int, only_unlearned: bool = False):
    if user_id not in user_vocabulary or not user_vocabulary[user_id]:
        return None
    
    if only_unlearned:
        unlearned_words = [w for w in user_vocabulary[user_id] if not w.get("learned", False)]
        if not unlearned_words:
            return None
        return random.choice(unlearned_words)
    
    return random.choice(user_vocabulary[user_id])

def update_accuracy(user_id: int, is_correct: bool):
    progress = get_user_progress(user_id)
    if not progress:
        return
    
    progress["total_attempts"] = progress.get("total_attempts", 0) + 1
    if is_correct:
        progress["correct_attempts"] = progress.get("correct_attempts", 0) + 1
        progress["current_streak"] = progress.get("current_streak", 0) + 1
        progress["exercises_completed"] = progress.get("exercises_completed", 0) + 1
    else:
        progress["current_streak"] = 0
    
    total = progress.get("total_attempts", 0)
    correct = progress.get("correct_attempts", 0)
    if total > 0:
        progress["accuracy"] = round(correct / total * 100, 1)

def increment_word_review(user_id: int, word: str):
    if user_id in user_vocabulary:
        for w in user_vocabulary[user_id]:
            if w.get("word") == word:
                w["review_count"] = w.get("review_count", 0) + 1
                if w["review_count"] >= 2:
                    w["learned"] = True
                return True
    return False

def mark_word_as_learned(user_id: int, word: str):
    if user_id in user_vocabulary:
        for w in user_vocabulary[user_id]:
            if w.get("word") == word:
                w["learned"] = True
                return True
    return False

def get_daily_phrases():
    all_phrases = [
        {"en": "How are you?", "ru": "Как дела?", "context": "Приветствие"},
        {"en": "I'm fine, thank you!", "ru": "Хорошо, спасибо!", "context": "Ответ на приветствие"},
        {"en": "What's your name?", "ru": "Как тебя зовут?", "context": "Знакомство"},
        {"en": "Nice to meet you!", "ru": "Приятно познакомиться!", "context": "Знакомство"},
        {"en": "Where are you from?", "ru": "Откуда ты?", "context": "Разговор о происхождении"},
        {"en": "Can you help me?", "ru": "Можешь помочь мне?", "context": "Просьба о помощи"},
        {"en": "I don't understand", "ru": "Я не понимаю", "context": "Непонимание"},
        {"en": "How much is it?", "ru": "Сколько это стоит?", "context": "Покупки"},
        {"en": "What time is it?", "ru": "Который час?", "context": "Время"},
        {"en": "Where is the bathroom?", "ru": "Где ванная комната?", "context": "Поиск места"},
        {"en": "I'm hungry", "ru": "Я голоден", "context": "Еда"},
        {"en": "Let's go!", "ru": "Пошли!", "context": "Предложение"},
        {"en": "See you later!", "ru": "Увидимся позже!", "context": "Прощание"},
        {"en": "Have a nice day!", "ru": "Хорошего дня!", "context": "Пожелание"},
        {"en": "You're welcome!", "ru": "Пожалуйста!", "context": "Ответ на спасибо"},
        {"en": "Excuse me", "ru": "Извините", "context": "Привлечение внимания"},
        {"en": "I love you", "ru": "Я тебя люблю", "context": "Чувства"},
        {"en": "Good luck!", "ru": "Удачи!", "context": "Пожелание"},
        {"en": "Happy birthday!", "ru": "С днем рождения!", "context": "Поздравление"},
        {"en": "Merry Christmas!", "ru": "С Рождеством!", "context": "Поздравление"}
    ]
    
    return random.sample(all_phrases, 5)