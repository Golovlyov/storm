import telebot
#import config
TOKEN='1496653409:AAFM67g9SLzJuD_4yE55F6tn2UIS2A4fF0w'# token Bot
import random

from telebot import types

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
    elif (message.text) == 'Рп1': bot.send_message(message.chat.id, "вул. Турівська, 4")
    elif (message.text) == 'Рп2': bot.send_message(message.chat.id, "бульв. Дружби народі, 4/6")
    elif (message.text) == 'Рп3': bot.send_message(message.chat.id, "шосе Набережне, 3")
    elif (message.text) == 'Рп4': bot.send_message(message.chat.id, "вул. софійська, 21")
    elif (message.text) == 'Рп5': bot.send_message(message.chat.id, "вул. Грушевського, 9")
    elif (message.text) == 'Рп6': bot.send_message(message.chat.id, "вул. Нестайка Всеволода")
    elif (message.text) == 'Рп7': bot.send_message(message.chat.id, "вул. Наумовича, 169")
    elif (message.text) == 'Рп8': bot.send_message(message.chat.id, "вул. Антоновича, 52")
    elif (message.text) == 'Рп9': bot.send_message(message.chat.id, "вул. Жилянська , 111")
    elif (message.text) == 'Рп10': bot.send_message(message.chat.id, "вул. Чорновола, 37")

    elif (message.text) == 'Рп11': bot.send_message(message.chat.id, "вул. Руставелі Шота, 10")
    elif (message.text) == 'Рп12': bot.send_message(message.chat.id, "вул. Інстітутська, 9")
    elif (message.text) == 'Рп13': bot.send_message(message.chat.id, "вул. Кірилівська, 83")
    elif (message.text) == 'Рп14': bot.send_message(message.chat.id, "вул. Бориспільська, 7")
    elif (message.text) == 'Рп15': bot.send_message(message.chat.id, "вул. Деміївська,33")
    elif (message.text) == 'Рп16': bot.send_message(message.chat.id, "вул. Коперника, 14")
    elif (message.text) == 'Рп17': bot.send_message(message.chat.id, "вул. Дегтярівська, 53")
    elif (message.text) == 'Рп18': bot.send_message(message.chat.id, "провул. Попова, 12")
    elif (message.text) == 'Рп19': bot.send_message(message.chat.id, "вул. Хрещатик, 15")
    elif (message.text) == 'Рп20': bot.send_message(message.chat.id, "провул. Гната Хоткевича, 6")

    elif (message.text) == 'Рп21': bot.send_message(message.chat.id, "провул. Гуцала Євгена, 3")
    elif (message.text) == 'Рп22': bot.send_message(message.chat.id, "вул. Предславинська, 28")
    elif (message.text) == 'Рп23': bot.send_message(message.chat.id, "просп. Повітрофлотський, 66")
    elif (message.text) == 'Рп24': bot.send_message(message.chat.id, "вул. Жуковського Василя, 22")
    elif (message.text) == 'Рп25': bot.send_message(message.chat.id, "вул. Волгоградська, 37")
    elif (message.text) == 'Рп26': bot.send_message(message.chat.id, "вул. Зоологічна, 3")
    elif (message.text) == 'Рп27': bot.send_message(message.chat.id, "вул. Політехнічна, 10")
    elif (message.text) == 'Рп28': bot.send_message(message.chat.id, "вул. Вітрука генерала,7А")
    elif (message.text) == 'Рп29': bot.send_message(message.chat.id, "шосе. Харківське, 210")
    elif (message.text) == 'Рп30': bot.send_message(message.chat.id, "вул. Ярославів Вал, 27")

    elif (message.text) == 'Рп31': bot.send_message(message.chat.id, "вул. Нагірна, 22")
    elif (message.text) == 'Рп32': bot.send_message(message.chat.id, "вул. Андріївська, 19")
    elif (message.text) == 'Рп33': bot.send_message(message.chat.id, "вул. Новокостянтинівська, 15")
    elif (message.text) == 'Рп34': bot.send_message(message.chat.id, "уточнити належність")
    elif (message.text) == 'Рп35': bot.send_message(message.chat.id, "уточнити належність")
    elif (message.text) == 'Рп36': bot.send_message(message.chat.id, "вул. Краківська, 10")
    elif (message.text) == 'Рп37': bot.send_message(message.chat.id, "просп. Миру, 7")
    elif (message.text) == 'Рп38': bot.send_message(message.chat.id, "вул. Йорданська, 28")
    elif (message.text) == 'Рп39': bot.send_message(message.chat.id, "бульв. Дружби народів, 25/31")
    elif (message.text) == 'Рп40': bot.send_message(message.chat.id, "просп. Перемоги, 53")

    elif (message.text) == 'Рп41': bot.send_message(message.chat.id, "вул. Мечникова, 13")
    elif (message.text) == 'Рп42': bot.send_message(message.chat.id, "уточнити належність")
    elif (message.text) == 'Рп43': bot.send_message(message.chat.id, "уточнити належність")
    elif (message.text) == 'Рп44': bot.send_message(message.chat.id, "вул.Автозаводська , 78")
    elif (message.text) == 'Рп45': bot.send_message(message.chat.id, "просп. Перемоги, 71/2")
    elif (message.text) == 'Рп46': bot.send_message(message.chat.id, "вул. Політехнічна, 10")
    elif (message.text) == 'Рп47': bot.send_message(message.chat.id, "вул. Притисько-микільська, 4")
    elif (message.text) == 'Рп48': bot.send_message(message.chat.id, "бульв. Чоколівський, 38")
    elif (message.text) == 'Рп49': bot.send_message(message.chat.id, "вул. Заслонова Костянтина, 9")
    elif (message.text) == 'Рп50': bot.send_message(message.chat.id, "вул. Подвойського, 8/10")

    elif (message.text) == 'Рп51': bot.send_message(message.chat.id, "вул. Качалова, 5")
    elif (message.text) == 'Рп52': bot.send_message(message.chat.id, "вул. Салютна, 12/62")
    elif (message.text) == 'Рп53': bot.send_message(message.chat.id, "бульв. Перова, 23")
    elif (message.text) == 'Рп54': bot.send_message(message.chat.id, "вул. Кримського академіка, 27")
    elif (message.text) == 'Рп55': bot.send_message(message.chat.id, "вул. Янтарна, 6")
    elif (message.text) == 'Рп56': bot.send_message(message.chat.id, "просп. Комарова космонавта, 1")
    elif (message.text) == 'Рп57': bot.send_message(message.chat.id, "вул. Освіти, 3А")
    elif (message.text) == 'Рп58': bot.send_message(message.chat.id, "вул. Здолбунівська, 2")
    elif (message.text) == 'Рп59': bot.send_message(message.chat.id, "вул. Гарматна, 2")
    elif (message.text) == 'Рп60': bot.send_message(message.chat.id, "уточнити належність")

    elif (message.text) == 'Рп61': bot.send_message(message.chat.id, "бульв. Лесі Українки, 26")
    elif (message.text) == 'Рп62': bot.send_message(message.chat.id, "бульв. Богдана Хмельницького, 23А")
    elif (message.text) == 'Рп63': bot.send_message(message.chat.id, "вул. Вітряні Гори, 2")
    elif (message.text) == 'Рп64': bot.send_message(message.chat.id, "вул. Героїв Севастополя, 13")
    elif (message.text) == 'Рп65': bot.send_message(message.chat.id, "вул. Бориспільська, 13")
    elif (message.text) == 'Рп66': bot.send_message(message.chat.id, "вул. Донця Михайла, 17-19")
    elif (message.text) == 'Рп67': bot.send_message(message.chat.id, "вул. Заболотного академика, 150Д")
    elif (message.text) == 'Рп68': bot.send_message(message.chat.id, "вул. Курська, 9")
    elif (message.text) == 'Рп69': bot.send_message(message.chat.id, "вул. Туполєва академіка, 18Г")
    elif (message.text) == 'Рп70': bot.send_message(message.chat.id, "вул. Крижановського академіка, 3")

    elif (message.text) == 'Рп71': bot.send_message(message.chat.id, "уточнити належність")
    elif (message.text) == 'Рп72': bot.send_message(message.chat.id, "вул. Воскресенська, 7")
    elif (message.text) == 'Рп73': bot.send_message(message.chat.id, "вул. Краснова Миколи, 27")
    elif (message.text) == 'Рп74': bot.send_message(message.chat.id, "вул. Братиславська, 8")
    elif (message.text) == 'Рп75': bot.send_message(message.chat.id, "вул. Плещеєва, 6")
    elif (message.text) == 'Рп76': bot.send_message(message.chat.id, "просп. Перемоги, 20")
    elif (message.text) == 'Рп77': bot.send_message(message.chat.id, "уточнити належність")
    elif (message.text) == 'Рп78': bot.send_message(message.chat.id, "вул. Юності, 7")
    elif (message.text) == 'Рп79': bot.send_message(message.chat.id, "вул. Бучми Амросія, 6А")
    elif (message.text) == 'Рп80': bot.send_message(message.chat.id, "") #конец

    elif (message.text) == 'Рп81': bot.send_message(message.chat.id, "вул. софійська, 21")
    elif (message.text) == 'Рп82': bot.send_message(message.chat.id, "вул. Грушевського, 9")
    elif (message.text) == 'Рп83': bot.send_message(message.chat.id, "вул. Нестайка Всеволода")
    elif (message.text) == 'Рп84': bot.send_message(message.chat.id, "вул. Наумовича, 169")
    elif (message.text) == 'Рп85': bot.send_message(message.chat.id, "вул. Турівська, 4")
    elif (message.text) == 'Рп86': bot.send_message(message.chat.id, "бульв. Дружби народі, 4/6")
    elif (message.text) == 'Рп87': bot.send_message(message.chat.id, "шосе Набережне, 3")
    elif (message.text) == 'Рп88': bot.send_message(message.chat.id, "вул. софійська, 21")
    elif (message.text) == 'Рп89': bot.send_message(message.chat.id, "вул. Грушевського, 9")
    elif (message.text) == 'Рп90': bot.send_message(message.chat.id, "вул. Нестайка Всеволода")

    elif (message.text) == 'Рп91': bot.send_message(message.chat.id, "вул. Наумовича, 169")
    elif (message.text) == 'Рп92': bot.send_message(message.chat.id, "вул. Грушевського, 9")
    elif (message.text) == 'Рп93': bot.send_message(message.chat.id, "вул. Нестайка Всеволода")
    elif (message.text) == 'Рп94': bot.send_message(message.chat.id, "вул. Наумовича, 169")
    elif (message.text) == 'Рп95': bot.send_message(message.chat.id, "вул. Турівська, 4")
    elif (message.text) == 'Рп96': bot.send_message(message.chat.id, "бульв. Дружби народі, 4/6")
    elif (message.text) == 'Рп97': bot.send_message(message.chat.id, "шосе Набережне, 3")
    elif (message.text) == 'Рп98': bot.send_message(message.chat.id, "вул. софійська, 21")
    elif (message.text) == 'Рп99': bot.send_message(message.chat.id, "вул. Грушевського, 9")
    elif (message.text) == 'Рп100': bot.send_message(message.chat.id, "вул. Нестайка Всеволода")

























    else:
        bot.send_message(message.chat.id, "Данні відсутні")




bot.polling(none_stop=True)

