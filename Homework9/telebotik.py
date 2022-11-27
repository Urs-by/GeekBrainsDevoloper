from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
import controller9


# t.me/gb_homework9_bot

# Define a few command handlers. These usually take the two arguments update and
# context.
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(
        rf"Привет {user.mention_html()}! Я бот, который умеет считать!",
        reply_markup=ForceReply(selective=True),
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("Для вычисления выражения введите данные, например 2*9 или 2/5 + 1/2")


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if '+' in update.message.text or '-' in update.message.text or '*' in update.message.text or '/' in update.message.text:
        result = controller9.bot_calculation(update.message.text)

        await update.message.reply_text(f"Результат вычисления равен {result}")
    else:
        await update.message.reply_text("Вы ввели не математическое выражение, попробуйте еще раз")


async def calc_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f"Введите выражение для подсчета")


def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    with open('token.txt', 'r') as new:
        my_token = new.readline()

    application = Application.builder().token(my_token).build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("calc", calc_command))

    # on non command i.e message - echo the message on Telegram
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Run the bot until the user presses Ctrl-C
    application.run_polling()


if __name__ == "__main__":
    main()


