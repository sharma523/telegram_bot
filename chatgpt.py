import telebot
from typing import Final

# Constants
TOKEN: Final = 'your_token'
BOT_USERNAME: Final = '@your_username'

# Initialize the bot
bot = telebot.TeleBot(TOKEN)

# Commands
@bot.message_handler(commands=['start'])
def start_command(message):
    bot.reply_to(message, 'Hello! Thanks for chatting with me! I am a banana!')

@bot.message_handler(commands=['help'])
def help_command(message):
    bot.reply_to(message, 'I am a simple bot! Use /start to greet me, or send a message like "hello" or "how are you".')

@bot.message_handler(commands=['custom'])
def custom_command(message):
    bot.reply_to(message, 'This is a custom command! Feel free to customize me!')

# Responses
def handle_response(text: str) -> str:
    processed: str = text.lower().strip()
    
    if 'hello' in processed:
        return 'I am good!'
    
    if 'how are you' in processed:
        return 'Fine, thanks for asking!'
    
    if 'who are you' in processed:
        return 'golu from amarpur'
    
    return 'I do not understand what you wrote...'

# Message Handler
@bot.message_handler(content_types=['text'])
def handle_message(message):
    message_type: str = message.chat.type
    text: str = message.text

    print(f'User ({message.chat.id}) in {message_type}: "{text}"')

    if message_type in ['group', 'supergroup']:
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)
    
    print(f'Bot: {response}')
    bot.reply_to(message, response)

# Error Handler
def error_handler(e):
    print(f'Error: {e}')

# Main
if __name__ == '__main__':
    print('Starting bot...')
    try:
        bot.infinity_polling()
    except Exception as e:
        error_handler(e)