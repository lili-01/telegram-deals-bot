from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends a message when the command /start is issued."""
    await update.message.reply_text('Hi! I am your deal notifier bot. Send /deal to get the latest deals.')

async def deal(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends a deal message when the command /deal is issued."""
    # Example deal message, replace this with your actual deal fetching logic
    deal_message = "Here's a fantastic deal on Crocs! 50% off: [Click here](http://example.com)"
    await update.message.reply_text(deal_message, parse_mode='Markdown')

def main() -> None:
    """Start the bot."""
    # Replace 'YOUR_TOKEN' with the token you got from BotFather
    TOKEN = '7314609137:AAFeWDECuNR9jMIwLAQQET7RTj2PE4DJsDw'
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(TOKEN).build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("deal", deal))

    # Run the bot until the user presses Ctrl-C
    application.run_polling()

if __name__ == '__main__':
    main()
