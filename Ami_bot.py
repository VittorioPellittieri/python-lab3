from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram.ext import CommandHandler
from telegram import ChatAction

def start(bot, update):
    update.message.reply_text("Benvenuto!")


def showtasks(bot, update):
    i = 1
    bot.sendChatAction(update.message.chat_id, ChatAction.TYPING)
    if (tasks.)
    strng = ""
    for task in sorted(tasks):
        strng = strng + str(i) + ". " + task + "\n"
        i = i + 1
    update.message.reply_text(strng)


def newTask(bot, update, args):
    task = ' '.join(args)
    tasks.append(task)
    update.message.reply_text("Task aggiunto!")


if __name__ == '__main__':
    """

    Apro file e immetto i task nella lista

    """

    file = open("task_list.txt", "r")
    tasks = []
    for line in file.readlines():
        tasks.append(line.strip())
    file.close()

    updater = Updater(token='783453175:AAHjW-bxeXjQ90ir9icmxh9-VDr5rKTzr1I')
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("showTasks", showtasks))
    dispatcher.add_handler(CommandHandler("newTask", newTask, pass_args=True))
    updater.start_polling()
    updater.idle()
