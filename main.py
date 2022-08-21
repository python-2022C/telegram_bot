import telegram
import os
TOKEN = os.environ['TOKEN']


bot = telegram.Bot(TOKEN)
user=bot.getUpdates()
u = telegram.Message(user)
print(u)
