import os
try:
    from bot import bot
    from helper import database as db
except ImportError:
    os.system("pip install pyTelegramBotAPI")
    os.system("pip install selenium")
except Exception as e:
    print(e)

try:
    db.createtable()
except Exception as e:
    pass

if __name__ == '__main__':
    bot.infinity_polling()


