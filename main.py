import telegram
import os
TOKEN = os.environ['TOKEN']


bot = telegram.Bot(TOKEN)
print(bot.getMe())
