import telebot
#import config
TOKEN='1496653409:AAFM67g9SLzJuD_4yE55F6tn2UIS2A4fF0w'# token Bot
import random

from telebot import types

#bot = telebot.TeleBot(config.TOKEN)
bot = telebot.TeleBot('1496653409:AAFM67g9SLzJuD_4yE55F6tn2UIS2A4fF0w')


@bot.message_handler(func=lambda message: True, content_types=['text'])

def lalala(message):


    if (message.text) == '36603649':
        bot.send_message(message.chat.id, "Головльов\n"
                                          "Олександр Едуардович ____гр 2 \n"
                                          "                                \n"
                                          "Ох Праці _______________15.09.2023\n"
                                          "Пож Безпека ___________15.09.2023\n"
                                          "ПТЕ ПУЕ \n"
                                          "Робота на висоті\n"
                                          "Робота з сосудами \n"
                                          "Робота з вогнем \n"
                                          "Опер права 10кВ\n"
                                          "Мед огляд _____________08.07.2023\n"
                                          "Високовольтні випроб\n")
        return
    elif (message.text) == '222':
        bot.send_message(message.chat.id, "Коваль\n"
                                          "Ігор Володимирович ____гр 5 \n"
                                          "                                \n"
                                          "Ох Праці _______________15.09.2023\n"
                                          "Пож Безпека ___________15.09.2023\n"
                                          "ПТЕ ПУЕ _______________15.09.2023\n"
                                          "Робота на висоті       \n"
                                          "Робота з сосудами      \n"
                                          "Робота з вогнем  \n"
                                          "Опер права 10кВ\n"
                                          "Мед огляд _____________08.07.2023\n"
                                          "Високовольтні випроб \n")

    elif (message.text) == '333':
        bot.send_message(message.chat.id, "Платонов\n"
                                          "Олександр Миколайович ____гр 3 \n"
                                          "                                \n"
                                          "Ох Праці _______________15.09.2023\n"
                                          "Пож Безпека ___________15.09.2023\n"
                                          "ПТЕ ПУЕ _______________15.09.2023\n"
                                          "Робота на висоті       \n"
                                          "Робота з сосудами      \n"
                                          "Робота з вогнем  \n"
                                          "Опер права 10кВ\n"
                                          "Мед огляд _____________08.07.2023\n"
                                          "Високовольтні випроб \n")
    elif (message.text) == '444':
        bot.send_message(message.chat.id, "Плахута\n"
                                          "Сергій Петрович ____гр 5 \n"
                                          "                                \n"
                                          "Ох Праці _______________15.09.2023\n"
                                          "Пож Безпека ___________15.09.2023\n"
                                          "ПТЕ ПУЕ _______________15.09.2023\n"
                                          "Робота на висоті       \n"
                                          "Робота з сосудами      \n"
                                          "Робота з вогнем  \n"
                                          "Опер права 10кВ\n"
                                          "Мед огляд _____________08.07.2023\n"
                                          "Високовольтні випроб \n")

    elif (message.text) == '555':
        bot.send_message(message.chat.id, "Богданенко\n"
                                          "Олексій Едуардович ____гр 2 \n"
                                          "                                \n"
                                          "Ох Праці _______________15.09.2023\n"
                                          "Пож Безпека ___________15.09.2023\n"
                                          "ПТЕ ПУЕ _______________15.09.2023\n"
                                          "Робота на висоті       \n"
                                          "Робота з сосудами      \n"
                                          "Робота з вогнем  \n"
                                          "Опер права 10кВ\n"
                                          "Мед огляд _____________08.07.2023\n"
                                          "Високовольтні випроб \n")
    elif (message.text) == 'Рп1':
        bot.send_message(message.chat.id, "вул. Турівська, 4")
    elif (message.text) == 'Рп2':
        bot.send_message(message.chat.id, "бульв. Дружби народі, 4/6")
    elif (message.text) == 'Рп3':
        bot.send_message(message.chat.id, "шосе Набережне, 3")
    elif (message.text) == 'Рп4':
        bot.send_message(message.chat.id, "вул. софійська, 21")
    elif (message.text) == 'Рп5':
        bot.send_message(message.chat.id, "вул. Грушевського, 9")
    elif (message.text) == 'Рп6':
        bot.send_message(message.chat.id, "вул. Нестайка Всеволода")
    elif (message.text) == 'Рп7':
        bot.send_message(message.chat.id, "вул. Наумовича, 169")


    else:
        bot.send_message(message.chat.id, "Данні відсутні")




bot.polling(none_stop=True)

