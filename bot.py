import telebot  # импортируем библиотеку телебота
from telebot import types  # из неё вытягиваем types

  # присоединяем токкен телебота который нам дал BotFaser
bot = telebot.TeleBot('5598060133:AAFVw9Xp12zeD1zUyAF7Sq7KRiuU7RmQX3Q')


@bot.message_handler(commands=['start'])
# функция start обрабатывает ввод кнопки /START и выводит сообщение - "В некоторых странах..."
# {message.from_user.first_name} - берет из сообщения пользователя его имя
# <b>__</b> - выделяет текст внутри жирным шрифтом
def star(message):
    mess = f'В некоторых странах я уже побывал и готов поделиться с тобой всем, что поможет тебе посетить их!) , ' \
           f'<b>{message.from_user.first_name}</b> выбери страну из списка ниже.'
    bot.send_message(message.chat.id, mess, parse_mode='html')

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    # Создаем переменную с указанием типа кнопки- подстрочная кнопка
    # (и указанием параметров - подстроения под экран, и колл-во кнопок в ряду)
    cuba = types.KeyboardButton('Куба')  # определяем кнопки и называем их
    georgia = types.KeyboardButton('Грузия')
    bali = types.KeyboardButton('Бали')
    morocco = types.KeyboardButton('Марокко')
    taiwan = types.KeyboardButton('Тайвань')
    seychelles = types.KeyboardButton('Сейшелы')
    portugal = types.KeyboardButton('Португалия')
    norway = types.KeyboardButton('Норвегия')
    greece = types.KeyboardButton('Греция')
    australia = types.KeyboardButton('Австралия')
    formentera = types.KeyboardButton('о. Форментера')

    keyboard.add(cuba, georgia, bali, morocco, taiwan, seychelles, portugal, norway, greece, australia, formentera)
    #  зарегистрировали кнопки
    bot.send_message(message.chat.id, 'Что выберешь?',
                     reply_markup=keyboard)  # выводим сообщение "что ты выберешь?" и активируем кнопку

    # сообщение от бота (с id чата, 'само сообщение', и прикрепление кнопки)


@bot.message_handler(content_types=['text'])
# content_types=['text'] - отслеживание ввода текста пользователем (ту кнопку с текстом которую пользователь нажимает)
def countries(message):
    if message.text == 'Грузия':
        web = types.InlineKeyboardMarkup()  # определение типа кнопки
        web.add(types.InlineKeyboardButton('Перейти на сайт',
                                           url='http://127.0.0.1:8000/georgia'))
        # регистрирование кнопки, название кнопки, и добавление в неё ссылки
        bot.send_message(message.chat.id, 'Про Грузию', reply_markup=web)
        # Сообщение от бота над кнопкой и её активация

        mon = types.InlineKeyboardMarkup()
        mon.add(types.InlineKeyboardButton('Перейти на сайт',
                                           url='https://wikiway.com/georgia/photo/'))
        bot.send_message(message.chat.id, 'Посмотреть фото Грузии', reply_markup=mon)

        gid = types.InlineKeyboardMarkup()
        gid.add(types.InlineKeyboardButton('Перейти на сайт',
                                           url='https://georgiabest.ru/?ysclid=l63hbu32ux720023035'))
        bot.send_message(message.chat.id, 'Гид-путеводитель по Грузии', reply_markup=gid)



    elif message.text == 'Куба':
        web = types.InlineKeyboardMarkup()

        web.add(
            types.InlineKeyboardButton('Перейти на сайт',
                                       url='http://127.0.0.1:8000/kuba'))
        bot.send_message(message.chat.id, 'Про Кубу', reply_markup=web)

        mon = types.InlineKeyboardMarkup()
        mon.add(types.InlineKeyboardButton('Перейти на сайт',
                                           url='https://wikiway.com/cuba/photo/'))
        bot.send_message(message.chat.id, 'Посмотреть фото Кубы', reply_markup=mon)

        gid = types.InlineKeyboardMarkup()
        gid.add(types.InlineKeyboardButton('Перейти на сайт',
                                           url='https://perito-burrito.com/posts/cubalibre?ysclid=l63hgmq38z991256268'))
        bot.send_message(message.chat.id, 'Гид-путеводитель по Кубе', reply_markup=gid)

    elif message.text == 'Бали':
        web = types.InlineKeyboardMarkup()

        web.add(
            types.InlineKeyboardButton('Перейти на сайт',
                                       url="http://127.0.0.1:8000/bali"))
        bot.send_message(message.chat.id, 'Про Индонезию,о.Бали', reply_markup=web)

        mon = types.InlineKeyboardMarkup()
        mon.add(types.InlineKeyboardButton('Перейти на сайт',
                                           url='https://wikiway.com/indonesia/ostrov-bali/photo/'))
        bot.send_message(message.chat.id, 'Посмотреть фото Бали', reply_markup=mon)

        gid = types.InlineKeyboardMarkup()
        gid.add(types.InlineKeyboardButton('Перейти на сайт',
                                           url='https://baliopen.ru/?ysclid=l63hk4wy9x620837921'))
        bot.send_message(message.chat.id, 'Гид-путеводитель по острову Бали', reply_markup=gid)

    elif message.text == 'Марокко':
        web = types.InlineKeyboardMarkup()

        web.add(
            types.InlineKeyboardButton('Перейти на сайт',
                                       url='http://127.0.0.1:8000/marokko'))
        bot.send_message(message.chat.id, 'Про Марокко', reply_markup=web)

        mon = types.InlineKeyboardMarkup()
        mon.add(types.InlineKeyboardButton('Перейти на сайт',
                                           url='https://wikiway.com/morocco/photo/'))
        bot.send_message(message.chat.id, 'Посмотреть фото Марокко', reply_markup=mon)

        gid = types.InlineKeyboardMarkup()
        gid.add(types.InlineKeyboardButton('Перейти на сайт',
                                           url='https://journal.travelmart.ru/marocco-guide?ysclid=l63hl4sxae3749260'))
        bot.send_message(message.chat.id, 'Гид-путеводитель по Марокко', reply_markup=gid)

    elif message.text == 'Тайвань':
        web = types.InlineKeyboardMarkup()

        web.add(
            types.InlineKeyboardButton('Перейти на сайт',
                                       url='http://127.0.0.1:8000/tayvan'))
        bot.send_message(message.chat.id, 'Про Тайвань', reply_markup=web)

        mon = types.InlineKeyboardMarkup()
        mon.add(types.InlineKeyboardButton('Перейти на сайт',
                                           url='https://wikiway.com/china/tayvan/photo/'))
        bot.send_message(message.chat.id, 'Посмотреть фото Тайваня', reply_markup=mon)

        gid = types.InlineKeyboardMarkup()
        gid.add(types.InlineKeyboardButton('Перейти на сайт',
                                           url='https://tonkosti.ru/%D0%A2%D0%B0%D0%B9%D0%B2%D0%B0%D0%BD%D1%8C?ysclid=l63hmsn5zy515091938'))
        bot.send_message(message.chat.id, 'Гид-путеводитель по Тайвани', reply_markup=gid)

    elif message.text == 'Сейшелы':
        web = types.InlineKeyboardMarkup()

        web.add(
            types.InlineKeyboardButton('Перейти на сайт',
                                       url='http://127.0.0.1:8000/seychelles'))
        bot.send_message(message.chat.id, 'Про Сейшельские острова', reply_markup=web)

        mon = types.InlineKeyboardMarkup()
        mon.add(types.InlineKeyboardButton('Перейти на сайт',
                                           url='https://wikiway.com/seychelles/photo/'))
        bot.send_message(message.chat.id, 'Посмотреть фото Сейшельских островов', reply_markup=mon)

        gid = types.InlineKeyboardMarkup()
        gid.add(types.InlineKeyboardButton('Перейти на сайт',
                                           url='https://thereminder.ru/puteshestvia/gid-po-sejshelskim-ostrovam-zachem-exat-tak-daleko?ysclid=l63hte4o5j750903559'))
        bot.send_message(message.chat.id, 'Гид-путеводитель по Сейшильским островам', reply_markup=gid)

    elif message.text == 'Португалия':
        web = types.InlineKeyboardMarkup()

        web.add(
            types.InlineKeyboardButton('Перейти на сайт',
                                       url='http://127.0.0.1:8000/portugalia'))
        bot.send_message(message.chat.id, 'Про Португалию', reply_markup=web)
        mon = types.InlineKeyboardMarkup()
        mon.add(types.InlineKeyboardButton('Перейти на сайт',
                                           url='https://wikiway.com/portugaliya/photo/'))
        bot.send_message(message.chat.id, 'Посмотреть фото Португалии', reply_markup=mon)

        gid = types.InlineKeyboardMarkup()
        gid.add(types.InlineKeyboardButton('Перейти на сайт',
                                           url='https://perito-burrito.com/posts/portugalguide?ysclid=l63hv302kw686098926'))
        bot.send_message(message.chat.id, 'Гид-путеводитель по Португалии', reply_markup=gid)

    elif message.text == 'Норвегия':
        web = types.InlineKeyboardMarkup()

        web.add(
            types.InlineKeyboardButton('Перейти на сайт',
                                       url='http://127.0.0.1:8000/norway'))
        bot.send_message(message.chat.id, 'Про Норвегию', reply_markup=web)

        mon = types.InlineKeyboardMarkup()
        mon.add(types.InlineKeyboardButton('Перейти на сайт',
                                           url='https://wikiway.com/norway/photo/'))
        bot.send_message(message.chat.id, 'Посмотреть фото Норвегии', reply_markup=mon)

        gid = types.InlineKeyboardMarkup()
        gid.add(types.InlineKeyboardButton('Перейти на сайт',
                                           url='https://www.tourister.ru/world/europe/norway?ysclid=l63hwkg5og456740638'))
        bot.send_message(message.chat.id, 'Гид-путеводитель по Норвегии', reply_markup=gid)

    elif message.text == 'Греция':
        web = types.InlineKeyboardMarkup()

        web.add(
            types.InlineKeyboardButton('Перейти на сайт',
                                       url='http://127.0.0.1:8000/grecia'))
        bot.send_message(message.chat.id, 'Про Грецию', reply_markup=web)

        mon = types.InlineKeyboardMarkup()
        mon.add(types.InlineKeyboardButton('Перейти на сайт',
                                           url='https://wikiway.com/greece/photo/'))
        bot.send_message(message.chat.id, 'Посмотреть фото Греции', reply_markup=mon)


        gid = types.InlineKeyboardMarkup()
        gid.add(types.InlineKeyboardButton('Перейти на сайт',
                                           url='https://www.greek.ru/tur/guide/'))
        bot.send_message(message.chat.id, 'Гид-путеводитель по Греции', reply_markup=gid)

    elif message.text == 'Австралия':
        web = types.InlineKeyboardMarkup()

        web.add(
            types.InlineKeyboardButton('Перейти на сайт',
                                       url='http://127.0.0.1:8000/australia'))
        bot.send_message(message.chat.id, 'Про Австралию', reply_markup=web)

        mon = types.InlineKeyboardMarkup()
        mon.add(types.InlineKeyboardButton('Перейти на сайт',
                                           url='https://wikiway.com/australia/photo/'))
        bot.send_message(message.chat.id, 'Посмотреть фото Австралии', reply_markup=mon)

        gid = types.InlineKeyboardMarkup()
        gid.add(types.InlineKeyboardButton('Перейти на сайт',
                                           url='https://tonkosti.ru/%D0%90%D0%B2%D1%81%D1%82%D1%80%D0%B0%D0%BB%D0%B8%D1%8F'))
        bot.send_message(message.chat.id, 'Гид-путеводитель по Австралии', reply_markup=gid)

    elif message.text == 'о. Форментера':
        web = types.InlineKeyboardMarkup()

        web.add(
            types.InlineKeyboardButton('Перейти на сайт',
                                       url='http://127.0.0.1:8000/formentera'))
        bot.send_message(message.chat.id, 'Про остров Форментера', reply_markup=web)

        mon = types.InlineKeyboardMarkup()
        mon.add(types.InlineKeyboardButton('Перейти на сайт',
                                           url='https://wikiway.com/spain/ostrov-formentera/photo/'))
        bot.send_message(message.chat.id, 'Посмотреть фото острова Форментера', reply_markup=mon)

        gid = types.InlineKeyboardMarkup()
        gid.add(types.InlineKeyboardButton('Перейти на сайт',
                                           url='https://tonkosti.ru/%D0%A4%D0%BE%D1%80%D0%BC%D0%B5%D0%BD%D1%82%D0%B5%D1%80%D0%B0?ysclid=l63i4ssvy9371713177'))
        bot.send_message(message.chat.id, 'Гид-путеводитель по острову Форментера', reply_markup=gid)


@bot.message_handler()
# сделали метод который отвечает за кнопку MENU (слева от строки ввода) которая отвечает за перезапуск программы - /START
def send_welcome(message: telebot.types.Message):
    bot.reply_to(message, message.text)


bot.set_my_commands([
    telebot.types.BotCommand("/start", "Перезапуск бота"),
])
# кнопка MENU (слева от строки ввода) которая отвечает за перезапуск программы - /START

bot.polling(none_stop=True)  # запуск чата на постоянное выполнение