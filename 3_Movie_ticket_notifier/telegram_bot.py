import telegram

bot = telegram.Bot(token='977420791:AAFP5flh1wz0_hhl-NFLNAfkpndE9IGcWo0')

for i in bot.getUpdates():
    print(i.message)

bot.sendMessage(chat_id = 642229581, text = "Test")
