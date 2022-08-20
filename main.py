import telegram
import os
TOKEN = os.environ['TOKEN']


bot = telegram.Bot(TOKEN)
user=bot.getMe()
print(user.username)
