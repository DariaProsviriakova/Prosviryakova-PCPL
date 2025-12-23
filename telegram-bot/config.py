
API_TOKEN = "8201918414:AAEAYeft2fkt9s2aYTWeYmrtQOc_XZfZUJM" 

VOCABULARY_BY_TOPIC = {
    "Еда": {
        "apple": {"ru": "яблоко", "examples": ["I eat an apple", "Red apple"]},
        "bread": {"ru": "хлеб", "examples": ["Fresh bread", "Slice of bread"]},
        "water": {"ru": "вода", "examples": ["Glass of water", "Drink water"]},
        "milk": {"ru": "молоко", "examples": ["Glass of milk", "Milk is white"]},
        "cheese": {"ru": "сыр", "examples": ["Piece of cheese", "Yellow cheese"]},
    },
    "Путешествия": {
        "airport": {"ru": "аэропорт", "examples": ["Go to airport", "Airport terminal"]},
        "hotel": {"ru": "отель", "examples": ["Book a hotel", "Hotel room"]},
        "ticket": {"ru": "билет", "examples": ["Buy ticket", "Ticket price"]},
        "passport": {"ru": "паспорт", "examples": ["My passport", "Show passport"]},
        "luggage": {"ru": "багаж", "examples": ["Check luggage", "Heavy luggage"]},
    },
    "Дом": {
        "house": {"ru": "дом", "examples": ["Big house", "My house"]},
        "room": {"ru": "комната", "examples": ["Clean room", "Living room"]},
        "kitchen": {"ru": "кухня", "examples": ["Kitchen table", "Cook in kitchen"]},
        "bathroom": {"ru": "ванная", "examples": ["Bathroom mirror", "Go to bathroom"]},
        "bedroom": {"ru": "спальня", "examples": ["Bedroom window", "Sleep in bedroom"]},
    },
    "Работа": {
        "office": {"ru": "офис", "examples": ["Office building", "Work in office"]},
        "meeting": {"ru": "встреча", "examples": ["Business meeting", "Schedule a meeting"]},
        "computer": {"ru": "компьютер", "examples": ["Computer screen", "Use computer"]},
        "salary": {"ru": "зарплата", "examples": ["Monthly salary", "Good salary"]},
        "colleague": {"ru": "коллега", "examples": ["Friendly colleague", "Talk to colleague"]},
    },
    "Образование": {
        "school": {"ru": "школа", "examples": ["Go to school", "School teacher"]},
        "university": {"ru": "университет", "examples": ["University student", "Study at university"]},
        "teacher": {"ru": "учитель", "examples": ["Math teacher", "Respect teacher"]},
        "student": {"ru": "студент", "examples": ["Good student", "Student life"]},
        "book": {"ru": "книга", "examples": ["Interesting book", "Read book"]},
    }
}

GRAMMAR_LESSONS = {
    "Present Simple": {
        "name": "Present Simple (Настоящее простое время)",
        "description": "Используется для регулярных действий, привычек и общих фактов",
        "rules": [
            " I/You/We/They + глагол без изменений",
            " He/She/It + глагол + s/es",
            " Отрицание: don't/doesn't + глагол",
            " Вопрос: Do/Does + подлежащее + глагол"
        ],
        "examples": [
            "I work every day. → Я работаю каждый день.",
            "She works in an office. → Она работает в офисе.",
            "They don't like coffee. → Они не любят кофе.",
            "Does he speak English? → Он говорит по-английски?"
        ],
        "usage": [
            "Регулярные действия и привычки",
            "Общие факты и истины",
            "Расписания и программы",
            "Действия по графику"
        ],
        "time_markers": [
            "always, usually, often",
            "sometimes, never",
            "every day/week/month",
            "on Mondays, in the morning"
        ]
    },
    "Past Simple": {
        "name": "Past Simple (Прошедшее простое время)",
        "description": "Используется для завершенных действий в прошлом",
        "rules": [
            " Правильные глаголы: глагол + ed",
            " Неправильные глаголы: 2-я форма глагола",
            " Отрицание: didn't + глагол (1-я форма)",
            " Вопрос: Did + подлежащее + глагол (1-я форма)"
        ],
        "examples": [
            "I worked yesterday. → Я работал вчера.",
            "She went to school. → Она пошла в школу.",
            "They didn't visit us. → Они не посетили нас.",
            "Did you see that film? → Ты видел этот фильм?"
        ],
        "usage": [
            "Завершенные действия в прошлом",
            "Последовательность действий",
            "Привычки в прошлом",
            "Конкретное время в прошлом"
        ],
        "time_markers": [
            "yesterday, last week",
            "in 2020, 5 years ago",
            "when I was young",
            "at 5 o'clock yesterday"
        ]
    },
    "Future Simple": {
        "name": "Future Simple (Будущее простое время)",
        "description": "Используется для действий в будущем, решений и предсказаний",
        "rules": [
            " Утверждение: will + глагол",
            " Отрицание: won't + глагол",
            " Вопрос: Will + подлежащее + глагол",
            " Сокращения: I'll, you'll, he'll"
        ],
        "examples": [
            "I will help you. → Я помогу тебе.",
            "She will be a doctor. → Она будет врачом.",
            "They won't come tomorrow. → Они не придут завтра.",
            "Will you marry me? → Ты выйдешь за меня?"
        ],
        "usage": [
            "Спонтанные решения",
            "Предсказания без доказательств",
            "Обещания и предложения",
            "Действия в будущем"
        ],
        "time_markers": [
            "tomorrow, next week",
            "in the future, soon",
            "in 2030, in 5 years",
            "later, tonight"
        ]
    },
    "Present Continuous": {
        "name": "Present Continuous (Настоящее продолженное время)",
        "description": "Используется для действий, происходящих прямо сейчас или в ближайшем будущем",
        "rules": [
            " Утверждение: am/is/are + глагол + ing",
            " Отрицание: am not/isn't/aren't + глагол + ing",
            " Вопрос: Am/Is/Are + подлежащее + глагол + ing"
        ],
        "examples": [
            "I am studying now. → Я учусь сейчас.",
            "He is watching TV. → Он смотрит телевизор.",
            "They aren't working today. → Они не работают сегодня.",
            "Are you listening to me? → Ты меня слушаешь?"
        ],
        "usage": [
            "Действия в момент речи",
            "Временные ситуации",
            "Изменяющиеся ситуации",
            "Запланированные будущие действия"
        ],
        "time_markers": [
            "now, at the moment",
            "currently, right now",
            "today, this week",
            "Look!, Listen!"
        ]
    },
    "Артикли": {
        "name": "Артикли (a/an/the)",
        "description": "Определенные и неопределенные артикли в английском языке",
        "rules": [
            " a - перед согласным звуком: a book, a university",
            " an - перед гласным звуком: an apple, an hour",
            " the - определенный артикль: the sun, the book I read",
            " Без артикля - общие понятия: love, water, English"
        ],
        "examples": [
            "I have a book. → У меня есть книга.",
            "She is an engineer. → Она инженер.",
            "The sun is bright. → Солнце яркое.",
            "I speak English. → Я говорю по-английски."
        ],
        "usage": [
            "a/an - один из многих (впервые упоминается)",
            "the - конкретный предмет (уже известен)",
            "— - неисчисляемые существительные",
            "— - названия стран, городов, языков"
        ],
        "exceptions": [
            "a university (согласный звук [j])",
            "an hour (гласный звук [aʊ])",
            "the USA (сокращения стран)",
            "the Netherlands (страны во мн. числе)"
        ],
        "features": [
            "a/an = один/какой-то",
            "the = конкретный/уже известный",
            "a/an + исчисляемые существительные",
            "the + уникальные предметы (the sun, the moon)"
        ]
    },
    "Предлоги": {
        "name": "Предлоги времени и места",
        "description": "Предлоги времени in/on/at и предлоги места",
        "rules": [
            " at - точное время: at 5 o'clock, at night",
            " on - дни и даты: on Monday, on 1st May",
            " in - месяцы, годы, периоды: in June, in 2024",
            " in - внутри: in the room, in the box",
            " on - на поверхности: on the table, on the wall",
            " at - у конкретного места: at home, at school"
        ],
        "examples": [
            "I get up at 7 AM. → Я встаю в 7 утра.",
            "We meet on Monday. → Мы встречаемся в понедельник.",
            "She was born in 1990. → Она родилась в 1990 году.",
            "The book is on the table. → Книга на столе.",
            "He lives in London. → Он живет в Лондоне.",
            "She is at the park. → Она в парке."
        ],
        "usage": [
            "at + время: at 3 PM, at midnight",
            "on + дни: on Friday, on my birthday",
            "in + периоды: in summer, in the morning",
            "in для больших пространств, at для точек",
            "on для поверхностей и улиц"
        ],
        "common_prepositions": [
            "in: in the car, in the city, in the world",
            "on: on the bus, on the street, on the floor",
            "at: at work, at the door, at the station",
            "to: go to school, come to me, return to home",
            "from: from Russia, from 9 to 5, from my friend"
        ]
    },
    "Модальные глаголы": {
        "name": "Модальные глаголы",
        "description": "Глаголы, выражающие возможность, необходимость, разрешение",
        "rules": [
            " can/could - умение, возможность",
            " may/might - разрешение, вероятность",
            " must - обязанность, необходимость",
            " should - совет, рекомендация",
            " will/would - будущее, вежливые просьбы",
            " Нет -s в 3-м лице: He can swim (NOT cans)",
            " Вопросы без do/does: Can you swim? (NOT Do you can swim?)"
        ],
        "examples": [
            "I can swim. → Я умею плавать.",
            "You must study. → Ты должен учиться.",
            "She should rest. → Ей следует отдохнуть.",
            "May I come in? → Можно войти?",
            "Could you help me? → Не могли бы вы помочь мне?",
            "It might rain tomorrow. → Возможно, завтра будет дождь."
        ],
        "usage": [
            "can - физическая возможность (I can speak English)",
            "could - вежливая просьба или прошлая возможность",
            "must - сильная необходимость (You must wear a seatbelt)",
            "should - рекомендация (You should see a doctor)",
            "may - формальное разрешение (May I leave the room?)",
            "might - небольшая вероятность (It might snow)"
        ],
        "features": [
            "Не добавляют -s в 3 лице (He can, NOT He cans)",
            "За ними глагол без to (I can swim, NOT I can to swim)",
            "Не используют вспомогательные глаголы в вопросах",
            "Имеют одинаковую форму для всех лиц",
            "Не имеют инфинитива и причастий"
        ],
        "negation": [
            "can → can't/cannot",
            "could → couldn't",
            "must → mustn't (запрет)",
            "should → shouldn't",
            "may → may not",
            "might → might not"
        ]
    },
}