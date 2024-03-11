import telebot
import comfig

bot = telebot.TeleBot(comfig.TOKEN)

@bot.message_handler(content_types=['text'])
def lalalal(message):
    bot.send_message(message.chat.id, message.text)

    # RUN
bot.polling(non_stop=True)