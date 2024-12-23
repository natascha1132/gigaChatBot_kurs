# Лексикон для текстовых сообщений
LEXICON: dict[str, str] = {
    "rewrite_text": "Введите текст, который нужно переписать:",
    "analyze_text": "Введите текст для анализа:",
    "summarize_text": "Введите текст для рерайта:",
    "show_statistics": "Вы выполнили 15 запросов.",
    "help": "Я могу переписывать тексты, анализировать их и создавать краткие изложения.\n"
            "Выберите нужный пункт в меню.",
    "start": "Привет! Я бот для работы с текстами. Выберите действие в меню.",
    "invalid_option": "Выберите опцию из меню или напишите /help для получения помощи."
}

# Лексикон команд
LEXICON_COMMANDS: dict[str, str] = {
    "/start": "Начало работы",
    "/help": "Справка",
    "/admin": "Показать статистику(только для админа)"
}
