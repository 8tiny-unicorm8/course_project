import telebot
from telebot import types

bot = telebot.TeleBot('5468268645:AAFcf6W2uD9K8sKwiVczkn4cK8VKMir034Y')

# @bot.message_handler(commands=['start'])
# def start(message):
#     mess = f'<b>Привет!</b> Я бот-турист.' \
#            f'В некоторых странах я уже побывал и готов поделиться с тобой всем что поможет тебе посетить их!) , ' \
#            f'<b>{message.from_user.first_name}</b> выбери страну из списка ниже'
#     bot.send_message(message.chat.id, mess, parse_mode='html')  # parse_mode='html'
#     # message.chat.id- через сообщение мы обратились к чату и получили его id
#     # mess - текст, который мы передаём.
#     # html - формат с тегами, с которыми м можем отправлять текст. например - <b> </b>
#     # {message.from_user.first_name} - метод получение имени пользователя.
#     keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
#     cuba = types.KeyboardButton('Куба')
#     georgia = types.KeyboardButton('Грузия')
#     bali = types.KeyboardButton('Бали')
#     morocco = types.KeyboardButton('Морокко')
#     taiwan = types.KeyboardButton('Тайвань')
#     seychelles = types.KeyboardButton('Сейшелы')
#     portugal = types.KeyboardButton('Португалия')
#     norway = types.KeyboardButton('Норвегия')
#     greece = types.KeyboardButton('Греция')
#     australia = types.KeyboardButton('Австралия')
#     keyboard.add(cuba, georgia, bali, morocco, taiwan, seychelles, portugal, norway, greece, australia)
#     bot.send_message(message.chat.id, 'Сделайте выбор',
#                      reply_markup=keyboard)
#
#     @bot.message_handler(content_types=['text'])  # content_types=['text'] - отслеживание ввода текста пользователем
#     def countries(message):
#         if message.text == 'Грузия':
#             web = types.InlineKeyboardMarkup()
#             web.add(
#                 types.InlineKeyboardButton('Перейти на сайт',
#                                            url='https://wikiway.com/georgia/'))
#             bot.send_message(message.chat.id, 'Про Грузию', reply_markup=web)
#
#             money = types.InlineKeyboardMarkup()
#             money.add(types.InlineKeyboardButton('Перейти на сайт',
#                                                  url='http://www.finmarket.ru/currency/rates/?id=10122&ysclid=l5p7ldbx6o773804645'))
#             bot.send_message(message.chat.id, 'Курсы валют в Грузии', reply_markup=money)
#
#             home = types.InlineKeyboardMarkup()
#             home.add(types.InlineKeyboardButton('Перейти на сайт', url=''))
#             bot.send_message(message.chat.id, 'Гостиницы/Хостелы', reply_markup=home)
#
#             places = types.InlineKeyboardMarkup()
#             places.add(types.InlineKeyboardButton('Перейти на сайт', url=''))
#             bot.send_message(message.chat.id, 'Что стоит посетить?', reply_markup=places)
#
#             guide = types.InlineKeyboardMarkup()
#             guide.add(types.InlineKeyboardButton('Перейти на сайт', url=''))
#             bot.send_message(message.chat.id, 'С гидом или без?', reply_markup=guide)
#
#             taxi = types.InlineKeyboardMarkup()
#             taxi.add(types.InlineKeyboardButton('Перейти на сайт', url=''))
#             bot.send_message(message.chat.id, 'Такси/Аренда авто', reply_markup=taxi)
#
#             sos = types.InlineKeyboardMarkup()
#             sos.add(types.InlineKeyboardButton('Перейти на сайт', url=''))
#             bot.send_message(message.chat.id, 'Экстренные службы', reply_markup=sos)
#
#         elif message.text == 'Бали':
#             web = types.InlineKeyboardMarkup()
#
#             web.add(
#                 types.InlineKeyboardButton('Перейти на сайт',
#                                            url='https://wikiway.com/indonesia/ostrov-bali/'))
#             bot.send_message(message.chat.id, 'Про Индонезию,о.Бали', reply_markup=web)
#
#             money = types.InlineKeyboardMarkup()
#             money.add(types.InlineKeyboardButton('Перейти на сайт',
#                                                  url='https://nashaplaneta.net/asia/indonesia/money?ysclid=l5pffd65fj327741919'))
#             bot.send_message(message.chat.id, 'Курсы валют в Индонезии', reply_markup=money)
#
#             home = types.InlineKeyboardMarkup()
#             home.add(types.InlineKeyboardButton('Перейти на сайт', url=''))
#             bot.send_message(message.chat.id, 'Гостиницы/Хостелы', reply_markup=home)
#
#             places = types.InlineKeyboardMarkup()
#             places.add(types.InlineKeyboardButton('Перейти на сайт', url=''))
#             bot.send_message(message.chat.id, 'Что стоит посетить?', reply_markup=places)
#
#             guide = types.InlineKeyboardMarkup()
#             guide.add(types.InlineKeyboardButton('Перейти на сайт', url=''))
#             bot.send_message(message.chat.id, 'С гидом или без?', reply_markup=guide)
#
#             taxi = types.InlineKeyboardMarkup()
#             taxi.add(types.InlineKeyboardButton('Перейти на сайт', url=''))
#             bot.send_message(message.chat.id, 'Такси/Аренда авто', reply_markup=taxi)
#
#             sos = types.InlineKeyboardMarkup()
#             sos.add(types.InlineKeyboardButton('Перейти на сайт', url=''))
#             bot.send_message(message.chat.id, 'Экстренные службы', reply_markup=sos)
#
#
# bot.polling(none_stop=True)  # запуск чата на постоянное выполнение



##############################################################
# @bot.message_handler(commands=['start'])   #otslezhiv komandu
# def start(message):
#     imja = f'Привет, <b>{message.from_user.first_name}</b>'
#     bot.send_message(message.chat.id, imja, parse_mode='html')
#
# def start_1(m):
#     keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     keyboard.add(*[types.KeyboardButton(name) for name in ['Куба']])
#     keyboard.add(*[types.KeyboardButton(name) for  name in ['Норвегия']])
#     keyboard.add(*[types.KeyboardButton(name) for  name in ['Бали']])
#     keyboard.add(*[types.KeyboardButton(name) for  name in ['Ничего не надо']])
#     bot.send_message(m.chat.id,  'ПРивет, выбери страну из списка:', reply_markup=keyboard)
#     #keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
#     norway = types.KeyboardButton('Норвегия')
#     countrys = {
#         norway: ['Стоимость посадки в такси - от 3 евро, а каждый последующий километр будет стоить от 1,3 евро.', 'link', 'прокат', 'Гостиницы стоят по-разному',
#                  'Экстренная оперативная служба - 112 \nПожарная служба - 110 \nПолиция - 112 \nСкорая медицинская помощь - 113 \nБереговая служба - 120 \n911 - перенаправляется на 112',
#                  'достопримечательности'],
#         'Бали': ['тест', 'тест2', 'тест3', 'тест4', 'тест5',
#              'тест6'],
# }
#
#     while True:
#         ch = int(input('Выберите страну из списка: \n1. Норвегия \n2. Бали \n3. Марокко \nВвод:'))
#         country = list(countrys.keys())[ch - 1]
#         print('Вы выбрали страну ', country, '.')
#
#         ch_1 = int(input('Что Вам необходимо узнать?:  \n1. Стоимость такси'))
#         print(ch_1)
#         print(countrys[country][ch_1 - 1])
#         if ch == 0:
#             print('Досвидос')
#             break


###################################################################################################

@bot.message_handler(commands=['start'])   #otslezhiv komandu
# def start(message):
#     imja = f'Привет, <b>{message.from_user.first_name}</b>'
#     bot.send_message(message.chat.id, imja, parse_mode='html')

def start_1(m):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in ['Куба']])
    keyboard.add(*[types.KeyboardButton(name) for  name in ['Норвегия']])
    keyboard.add(*[types.KeyboardButton(name) for  name in ['Бали']])
    keyboard.add(*[types.KeyboardButton(name) for  name in ['Ничего не надо']])
    bot.send_message(m.chat.id,  'ПРивет, выбери страну из списка:', reply_markup=keyboard)

@bot.message_handler(content_types=['text'])
def message(message):
    if message.text == 'Куба':
        keybordgosstart = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keybordgosstart.add(*[types.KeyboardButton(name) for name in ['Taxi', 'Foto']])
        # keybordgosstart.add(*[types.KeyboardButton(name) for name in ['Foto']])
        # keybordgosstart.add(*[types.KeyboardButton(name) for name in ['Sos']])
        bot.send_message(message.chat.id, 'Что хочешь узнать?', reply_markup=keybordgosstart)
    if message.text == 'Норвегия':
        keybordgosstart = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keybordgosstart.add(*[types.KeyboardButton(name) for name in ['Сос', 'Шашлындос']])
        # keybordgosstart.add(*[types.KeyboardButton(name) for name in ['Foto']])
        # keybordgosstart.add(*[types.KeyboardButton(name) for name in ['Sos']])
        bot.send_message(message.chat.id, 'Что хочешь узнать?', reply_markup=keybordgosstart)
    if message.text == 'Бали':
        keybordgosstart1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keybordgosstart1.add(*[types.KeyboardButton(name) for name in ['Такси', 'Фото']])
        # keybordgosstart.add(*[types.KeyboardButton(name) for name in ['Foto']])
        # keybordgosstart.add(*[types.KeyboardButton(name) for name in ['Sos']])
        bot.send_message(message.chat.id, 'Что хочешь узнать?', reply_markup=keybordgosstart1)

    elif message.text == 'Ничего не надо':
        bot.send_message(message.chat.id, 'хорошего дня,пока')

        @bot.message_handler(message)  # content_types=['text'] - отслеживание ввода текста пользователем
        def countries(message):
            if message.text == 'Куба' and keybordgosstart =='Taxi':
                web = types.InlineKeyboardMarkup()
                web.add(

                    types.InlineKeyboardButton('Перейти на сайт',


                                                url='https://wikiway.com/georgia/'))
                bot.send_message(message.chat.id, 'Такси', reply_markup=web)



                # money = types.InlineKeyboardMarkup()
                # money.add(types.InlineKeyboardButton('Перейти на сайт',
                #                                      url='http://www.finmarket.ru/currency/rates/?id=10122&ysclid=l5p7ldbx6o773804645'))
                # bot.send_message(message.chat.id, 'Курсы валют в Грузии', reply_markup=money)
                #
                # home = types.InlineKeyboardMarkup()
                # home.add(types.InlineKeyboardButton('Перейти на сайт', url=''))
                # bot.send_message(message.chat.id, 'Гостиницы/Хостелы', reply_markup=home)
                #
                # places = types.InlineKeyboardMarkup()
                # places.add(types.InlineKeyboardButton('Перейти на сайт', url=''))
                # bot.send_message(message.chat.id, 'Что стоит посетить?', reply_markup=places)
                #
                # guide = types.InlineKeyboardMarkup()
                # guide.add(types.InlineKeyboardButton('Перейти на сайт', url=''))
                # bot.send_message(message.chat.id, 'С гидом или без?', reply_markup=guide)
                #
                # taxi = types.InlineKeyboardMarkup()
                # taxi.add(types.InlineKeyboardButton('Перейти на сайт', url=''))
                # bot.send_message(message.chat.id, 'Такси/Аренда авто', reply_markup=taxi)
                #
                # sos = types.InlineKeyboardMarkup()
                # sos.add(types.InlineKeyboardButton('Перейти на сайт', url=''))
                # bot.send_message(message.chat.id, 'Экстренные службы', reply_markup=sos)



########################################################################################################
        # def h_text(message):
        #     if message.text.strip() == 'Taxi':
        #         answer = 'po 110ue'
        #     elif message.text.strip == 'Foto':
        #         answer = 'Fotochki0'
        #     bot.send_message(message.chat.id, 'po 100')



# @bot.message_handler(commands='Taxi')
# def Taxi(message):
#     markup = types.InlineKeyboardMarkup()
#     markup.add(types.InlineKeyboardButton('посетить сайт', url='https://developer.mozilla.org/ru/docs/Web/HTML/Element/br'))
#     bot.send_message(message.chat.id, 'pereydi na sait',reply_markup=markup)










# def start(message):
#     imja = f'Привет, <b>{message.from_user.first_name}, Выбери страну из списка: Norway, Bali, Kuba </b>'
#     bot.send_message(message.chat.id, imja, parse_mode='html')
#
#
# @bot.message_handler(commands=['Bali'])
# def Bali(message):
#     knopka = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
#     a = types.KeyboardButton('Такси инфа')
#     b = types.KeyboardButton('Фотки с координатами')
#     knopka.add(a, b)
#     bot.send_message(message.chat.id, 'Vibery stranu', reply_markup=knopka)
#
#
#
#
#
# @bot.message_handler(commands=['Norway'])
# def Norvay(message):
#     knopka = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
#     a = types.KeyboardButton('Taxi info')
#     b = types.KeyboardButton('foto s coord')
#     knopka.add(a, b)
#     bot.send_message(message.chat.id, 'Vibery stranu', reply_markup=knopka)
#
# @bot.message_handler(commands=['Kuba'])
# def Kuba(message):
#     knopka = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
#     a = types.KeyboardButton('Choto')
#     b = types.KeyboardButton('sos')
#     knopka.add(a, b)
#     bot.send_message(message.chat.id, 'Vibery stranu', reply_markup=knopka)



# @bot.message_handler()   #otslezhiv vvedenniy tekst
# def vvedtext(message):
# #while True:
#     if message.text == "Norvey":
#         bot.send_message(message.chat.id, 'Выбери что интересует: такси, гостиница, фото',
#                          parse_mode='html')
#
#     elif message.text == 'Bali':
#         bot.send_message(message.chat.id, 'Выбери что интересует: more, gori, pljazh',
#                          parse_mode='html')
#     elif message.text == 'Kuba':
#         bot.send_message(message.chat.id, 'это пока текст чтобы было понятно',
#                          parse_mode='html')
#     else:
#         bot.send_message(message.chat.id, 'В такой стране я небыл', parse_mode='html')
#         breakpoint()

# class Norway:
#     def Taxi(self):
#         print('Стоимость такси от 1 до 100 уе')
#
#     def Photo(self):
#         print('link')
#
#     def Auto(self):
#         print('прокат')
#
#     def Hotels(self):
#         print('Гостиницы стоят по-разному')
#
#     def Sos(self):
#         print('службы можно вызвать')
#
#     def Places(self):
#         print('достопримечательности')
#
# norway = Norway()
# norway.Auto()
# norway.Sos()
# norway.Places()
# norway.Taxi()
# #
# while True:
#     ch = int(input('Выберите страну из списка: \n1. Норвегия \n2. Бали \n3. Марокко \nВвод:'))
#     # ch_1 = Norway()
#     if ch == 1:
#         print('Ноpвегия. 1. bla')
#         ch_1 = int(input('Usluga: '))
#         if ch_1 == 1:
#             norway.Taxi()
#         elif ch_1 == 2:
#             norway.Sos()
#         elif ch_1 == 0:
#             print(ch)
#     elif ch == 0:
#         print('Досвидос')
#         break
@bot.message_handler()
def send_welcome(message: telebot.types.Message):
    bot.reply_to(message, message.text)


bot.set_my_commands([
    telebot.types.BotCommand("/start", "Перезапуск бота"),
])

bot.polling(none_stop=True)
