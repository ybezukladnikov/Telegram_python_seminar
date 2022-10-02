from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler, ConversationHandler
from config import TOKEN

bot = Bot(token=TOKEN)
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher


def start(update, context):
    arg = context.args
    print(arg)
    if not arg:
        context.bot.send_message(update.effective_chat.id, "Привет")
    else:
        context.bot.send_message(update.effective_chat.id, f"{' '.join(arg)}")


def info(update, context):
    context.bot.send_message(update.effective_chat.id,
                             """Доступны следующие команды:
                             /start - эхобот, повторяет всё сказанное через пробел,
                             /info - информация,
                             /add - добавить задачу""")


def message(update, context):
    text = update.message.text
    if text.lower() == 'привет':
        context.bot.send_message(update.effective_chat.id, 'Привет..')
    else:
        context.bot.send_message(update.effective_chat.id, 'я тебя не понимаю')


def unknown(update, context):
    context.bot.send_message(update.effective_chat.id, f'Шо сказал, не пойму')


def give_word(update, context):
    word = update.message.text
    if "бар" in word:
        joke = '''Белый медведь заходит в паб и говорит бармену:
                - Дайте мне виски и... кока-колу.
                - А почему такая пауза? - спрашивает бармен.
                - Это всё, что вас удивляет? - с обидой говорит медведь.'''
        context.bot.send_message(update.effective_chat.id, joke)
        return joke
    elif "пока" in word:
        context.bot.send_message(update.effective_chat.id, 'Покачивай шляпой из бара')
        return word
    context.bot.send_message(update.effective_chat.id, 'Вы, как всегда, правы, милорд')


start_handler = CommandHandler('start', start)
info_handler = CommandHandler('info', info)
message_handler = MessageHandler(Filters.text, give_word)
unknown_handler = MessageHandler(Filters.command, unknown)  # /game

dispatcher.add_handler(start_handler)
dispatcher.add_handler(info_handler)
# dispatcher.add_handler(conv_handler)
dispatcher.add_handler(unknown_handler)
dispatcher.add_handler(message_handler)

print('server started')
updater.start_polling()
updater.idle()

'''
Напишите программу, удаляющую из текста все слова, содержащие "абв".
'''
