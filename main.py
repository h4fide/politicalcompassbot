import os
try:
    from politicalbot import bot
except ImportError:
    os.system("pip install pyTelegramBotAPI")
    os.system("pip install selenium")


if __name__ == '__main__':
    bot.infinity_polling()
