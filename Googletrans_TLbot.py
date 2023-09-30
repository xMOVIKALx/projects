import telepot
from googletrans import Translator

translator = Translator()

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    chat_id = msg["chat"]["id"]
    text = msg["text"]
  
    if text.startswith("/"):
        command = text.split()[0]
        if command == "/translate":
            try :
                word = text[len(command):].strip()
                lang = translator.detect(word).lang
                if lang == "fa":
                    dest = "en"
                else:
                    dest = "fa"
                translation = translator.translate(word, dest=dest).text
                bot.sendMessage(chat_id, translation)
            except :
                bot.sendMessage(chat_id,"Please fill after /translate command.")
