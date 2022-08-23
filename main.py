import telegram
import os
TOKEN = os.environ['TOKEN']


bot = telegram.Bot(TOKEN)
updates=bot.getUpdates()
first_update = updates[0]
print(first_update.message.from_user.last_name)
