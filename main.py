import telegram
import os
TOKEN = os.environ['TOKEN']


bot = telegram.Bot(TOKEN)
updates=bot.getUpdates()
last_update = updates[-1]
chat_id = last_update.message.from_user.id
text = last_update.message.text
bot.sendMessage(chat_id, text)
