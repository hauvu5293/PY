import logging
from telegram.ext import Updater, CommandHandler

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Define your handler functions for each command
def start(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="Welcome to my voting bot!")

def vote(update, context):
    # Extract the vote from the user's message and save it to a database or file
    vote = update.message.text.replace("/vote ", "")
    context.bot.send_message(chat_id=update.message.chat_id, text="You voted for " + vote)

# Set up your bot
def main() -> None:
    updater = Updater("YOUR_TOKEN_HERE", use_context=True)

    # Add your command handlers
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CommandHandler('vote', vote))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
