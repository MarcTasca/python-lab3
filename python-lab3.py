from telegram.ext import Updater, CommandHandler
import List
from sys import argv

#creo la lista e la riempo con il file passato da line di comando
#variabile globale, probabilmente poco elegante, ma veloce e semplice
list=List.create_list(argv[1])

#estraggo il messaggio dopo il comando
def extract_text(string):
    command,text=string.split(' ', 1)
    return text

#aggiungo una task
def newTask(bot,update):
    task=extract_text(update.message.text)
    List.add_task(list,task)
    update.message.reply_text("task successfully added!")
    List.save_list(list,argv[1])

#mostro le task
def showTasks(bot,update):
    sorted_list=List.show_tasks(list)
    if sorted_list==None:
        message='nothing to show'
    else:
        message=sorted_list
    update.message.reply_text(message)

#rimuovo una task
def removeTask(bot,update):
    task = extract_text(update.message.text)
    if List.remove_task(list,task)==1:
        message='task successfully removed!'
    else:
        message='nothing to remove'
    update.message.reply_text(message)
    List.save_list(list, argv[1])

#rimuovo le task con all'interno la stringa
def removeAllTasks(bot,update):
    substring = extract_text(update.message.text)
    removed=List.remove_task_substring(list,substring)
    if len(removed) == 0:
        message='nothing to remove'
    else:
        message=removed
    update.message.reply_text(message)
    List.save_list(list, argv[1])

#main con i singal handler e l'avvio del bot tramite token
if __name__=='__main__':
    updater=Updater("579879753:AAHvYnM7J8QBwhp51YldYmZy-7vgnDqbMDs")
    dp=updater.dispatcher

    dp.add_handler(CommandHandler('newtask',newTask))
    dp.add_handler(CommandHandler('showtasks', showTasks))
    dp.add_handler(CommandHandler('removetask', removeTask))
    dp.add_handler(CommandHandler('removealltasks', removeAllTasks))

    updater.start_polling()
    updater.idle()
