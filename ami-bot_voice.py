from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
#la variabile update nelle funzioni è un pacchetto contentente tutto ciò che ci serve, preso da updater suppongo
#importare azioni della chat da pacchetto telegram
from telegram import ChatAction
from gtts import gTTS

#funzione invocata dal CH che fa risponde il bot con la funzione reply_text
def start(bot,update):
    update.message.reply_text('Hello!')

#update.message.text contiene il testo che è stato scritto al bot
#lo stesso testo viene inviato dal bot verso chi l'ha scritto
def echo(bot, update):
    #metodo per far vedere che sta scrivendo, ci serve sapere l'id della chat, e l'azione da inviare
    bot.sendChatAction(update.message.chat_id,ChatAction.UPLOAD_AUDIO)
    repeat_text=update.message.text
    tts= gTTS(text=repeat_text,lang='en')
    tts.save('echo.mp3')
    bot.sendVoice(update.message.chat_id,voice=open('echo.mp3','rb'))

    pass

def main():
    #creo l'oggetto per poi aprire la connessione
    updater=Updater("579879753:AAHvYnM7J8QBwhp51YldYmZy-7vgnDqbMDs")

    #creo l'ggetto dispatcher per gestire le chiamate
    dp=updater.dispatcher

    #aggiungo la gestione di una chiamata, invocando una funzione start
    #tramite una funzione importata da telegram.ext, che si chiama CommandHandler
    #la funzione contiene il comando ricevuto, a cui associa il nome della funzione da invocare
    dp.add_handler(CommandHandler('start',start))

    #serve per gestire i messaggi che non sono comandi
    #il primo campo filtra il tipo di messaggio che ci interessa, in questo caso text, testuale
    #il secondo campo invoca la funzione appropriata, Filters è da importare
    dp.add_handler(MessageHandler(Filters.text , echo))
    # comincia a chiedere se ci sono novità al server
    updater.start_polling()

    #nasconde gli errori che vengono mostrati quando stoppo il programma (che comunque non venivano mostrati)
    updater.idle()


if __name__ == '__main__':
    main()
