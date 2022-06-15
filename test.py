import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, filters, MessageHandler


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(update.message.chat.id, "Hello, I'm a weather bot.\nText the name of the city where"
                                                           " you want to find a current weather.\n"
                                                           "P.S. You should use only English names")


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    your_API_code = 'API_code'
    city = update.message.text.title()
    response = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={your_API_code}'
    )
    if response:
        response = response.json()
        await context.bot.send_message(update.message.chat.id, f"Temperature in {city}, {response['sys']['country']} is"
                                                               f" {response['main']['temp']}\u2103")
    else:
        await context.bot.send_message(update.message.chat.id, "The city is not found.\nPlease, try again.")

application = ApplicationBuilder().token('TOKEN').build()


application.add_handler(CommandHandler('start', start))
application.add_handler(MessageHandler(filters.TEXT, echo))

application.run_polling()
