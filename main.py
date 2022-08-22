import telegram
import os
TOKEN = os.environ['TOKEN']


bot = telegram.Bot(TOKEN)
user=bot.getUpdates()
print(user[0].fromDict())
