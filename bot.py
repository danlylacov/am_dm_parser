import telebot



token = '5159594918:AAGpVlavozfBPkTfqzNqvWwpoYTZNd_CFYE'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('Поиск по песне', 'Поиск по исполнителю')
    keyboard.add('О боте, поддержка')
    bot.send_message(message.chat.id, 'ПРИВЕТ, '+message.chat.first_name+'!\nЯ бот по поиску аккордов, табулатур для песен!\nИнстукция по использованию:\n\n1) выберете, как вы хотите начать поиск:\n         по исполнителю\n         по песне\n\n2) Нажмите на соответствующую кнопку\n\n3) Напишите исполнителя/название песни\n\n 4) Подождите пока запрос обрабатывается(примерное время ожидания 15 сек)\n\n\n\n\nПо воросам сотрудничества:\nEmail: danlylacov@yandex.ru\ntel:+7-952-098-71-30(telegram, whats app)', reply_markup=keyboard)
    bot.send_photo(message.chat.id, open('1.png', 'rb'))

bot.polling()