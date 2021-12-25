from translate import translate
import telebot

TOKEN = "5039566479:AAGINHjFdCE1Y7bjRoulTynUYkGgDx7pxcY"
tarjimonbot = telebot.TeleBot(token=5039566479:AAGINHjFdCE1Y7bjRoulTynUYkGgDx7pxcY)

# \start komandasi uchun mas'ul funksiya
@tarjimonbot.message_handler(commands=["start"])
def salom(message):
    xabar = "Assalomu alaykum, tarjimon botiga xush kelibsiz."
    xabar += "\nMatningizni yuboring."
    tarjimonbot.reply_to(message, xabar)


# matnlar uchun mas'ul funksiya
@tarjimonbot.message_handler(func=lambda msg: msg.text is not None)
def tarjima(message):
    msg = message.text
    tarjimonbot.reply_to(message, translate(msg))


tarjimonbot.polling()



