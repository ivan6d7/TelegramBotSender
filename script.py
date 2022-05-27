import telegram

API_KEY="5330860466:AAFRdtZyR9Gb1D6tS7ElgfViEPf0c9GsTMA"


bot = telegram.Bot(API_KEY)
def sendMessage(text, bot = bot):
    bot.send_message('1361694706', text)

