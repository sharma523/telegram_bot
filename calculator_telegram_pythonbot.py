import telebot
Token ="your_token"

bot =telebot.TeleBot(Token)
@bot.message_handler(['start'])
def start(message):
    bot.reply_to(message,"welcome to the bot")

@bot.message_handler(['help'])
def help(message):
    bot.reply_to(message,""" /start -> Greeting 
                 /help -> will give you all command list
                  if you want to use it as calculator then feel free""")
    
@bot.message_handler()
def custom(message):
   
    try:
        msg= eval(message.text.strip())
    except Exception as e:
        msg ="this can,t replay"
    bot.reply_to(message,msg)
bot.polling()