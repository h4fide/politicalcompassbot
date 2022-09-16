import sys
import telebot
from telebot import types
from config import token
import politicwebspost as pwp
import language as lang
bot = telebot.TeleBot(token)

choosenlanglist = []
choosenlang = choosenlanglist[0]

choosenlanglist.append('en')

def_questions = eval(f'lang.def_questions_{choosenlang}')
questionlang = eval(f'lang.question_{choosenlang}')
wronginput = eval(f'lang.wronginput_{choosenlang}')
elr = eval(f'lang.elr_msg_{choosenlang}')
sla = eval(f'lang.sla_msg_{choosenlang}')

answers = []

def catn(replay):
    if replay == eval(f'lang.s_disagree_{choosenlang}'):
        return 0
    elif replay == eval(f'lang.disagree_{choosenlang}'):
        return 1
    elif replay == eval(f'lang.agree_{choosenlang}'):
        return 2
    elif replay == eval(f'lang.s_agree_{choosenlang}'):
        return 3
    else:
        return 'error'

def rkm():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=False)
    strong_disagree = eval(f'lang.s_disagree_{choosenlang}')
    disagree = eval(f'lang.disagree_{choosenlang}')
    agree = eval(f'lang.agree_{choosenlang}')
    strong_agrre = eval(f'lang.s_agree_{choosenlang}')
    markup.add(strong_disagree)
    markup.add(disagree)
    markup.add(agree)
    markup.add(strong_agrre)
    return markup

@bot.message_handler(commands=['lang'])
def language_bot(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=False)
    markup.add('English')
    markup.add('Arabic')
    bot.send_message(message.chat.id, eval(f'lang.chooselang_{choosenlang}'), reply_markup=markup)
    bot.register_next_step_handler(message, language_bot2)

def language_bot2(message):
    if message.text == 'English':
        choosenlang = 'en'
        choosenlanglist.clear()
        choosenlanglist.append(choosenlang)
        bot.send_message(message.chat.id, 'Language changed to English')
        start_message(message)
    elif message.text == 'Arabic':
        choosenlang = 'ar'
        choosenlanglist.clear()
        choosenlanglist.append(choosenlang)
        bot.send_message(message.chat.id, 'تم تغيير اللغة الى العربية')
        start_message(message)

    else:
        bot.send_message(message.chat.id, eval(f'lang.wrnglanginput_{choosenlang}'))
        bot.register_next_step_handler(message, language_bot2)


@bot.message_handler(commands=['help'])
def help_message(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=1)
    markup.add(eval(f'lang.start_btn_{choosenlang}'))
    bot.send_message(message.chat.id,eval(f'lang.help_msg_{choosenlang}') , reply_markup=markup)

@bot.message_handler(commands=['cancel'])
def cancel_message(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=1)
    markup.add(eval(f'lang.start_btn_{choosenlang}'))
    bot.send_message(message.chat.id, eval(f'lang.canceled_{choosenlang}'), reply_markup=markup)


@bot.message_handler(commands=['start'])
def start_message(message):
    answers.clear()
    bot.reply_to(message, eval(f'lang.starting_msg_{choosenlang}'))
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=False)
    markup.add(eval(f'lang.letsgo_btn_{choosenlang}'))
    bot.send_message(message.chat.id, eval(f'lang.ready_msg_{choosenlang}'), reply_markup=markup)
    bot.register_next_step_handler(message, question1)

@bot.message_handler(func=lambda message: True)
def messagess(message):
    if message.text == eval(f'lang.restart_btn_{choosenlang}') or message.text == eval(f'lang.start_btn_{choosenlang}'):
        start_message(message)
    else:
        bot.reply_to(message, eval(f'lang.needhelp_msg_{choosenlang}'))

def question1(message):
    if message.text.startswith('/'):
        cancel_message(message)
    else:    
        bot.send_message(message.chat.id, eval(f'lang.journeycancel_msg_{choosenlang}'))
        bot.send_message(message.chat.id, eval(f'lang.part1_msg_{choosenlang}'))
        bot.send_message(message.chat.id, f'{questionlang} 1:\n{def_questions[1]}', reply_markup=rkm())
        bot.register_next_step_handler(message, question2)
    
def question2(message):
    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    if message.text == '/cancel':
        cancel_message(message)
    else:
        bot.send_message(message.chat.id, f'{questionlang} 2:\n{def_questions[2]}', reply_markup=rkm())
        if catn(message.text) == 'error':
            bot.send_message(message.chat.id, f'{wronginput}')
            bot.register_next_step_handler(message, question2)
        else:
            answers.append({1: catn(message.text)})
            bot.register_next_step_handler(message, question3)

def question3(message):
    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    if message.text == '/cancel':
        cancel_message(message)
    else:
        bot.send_message(message.chat.id, f'{questionlang} 3:\n{def_questions[3]}', reply_markup=rkm())
        if catn(message.text) == 'error':
            bot.send_message(message.chat.id, f'{wronginput}')
            bot.register_next_step_handler(message, question3)
        else:
            answers.append({2: catn(message.text)})
            bot.register_next_step_handler(message, question4)

def question4(message):
    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    bot.send_message(message.chat.id, f'{questionlang} 4:\n{def_questions[4]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, f'{wronginput}')
        bot.register_next_step_handler(message, question4)
    elif message.text == '/cancel':
        cancel_message(message)
    else:
        answers.append({3: catn(message.text)})
        bot.register_next_step_handler(message, question5)

def question5(message):
    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    bot.send_message(message.chat.id, f'{questionlang} 5:\n{def_questions[5]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, f'{wronginput}')
        bot.register_next_step_handler(message, question5)
    else:
        answers.append({4: catn(message.text)})
        bot.register_next_step_handler(message, question6)

def question6(message):
    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    bot.send_message(message.chat.id, f'{questionlang} 6:\n{def_questions[6]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, f'{wronginput}')
        bot.register_next_step_handler(message, question6)
    else:
        answers.append({5: catn(message.text)})
        bot.register_next_step_handler(message, question7)

def question7(message):
    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    bot.send_message(message.chat.id, f'{questionlang} 7:\n{def_questions[7]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, f'{wronginput}')
        bot.register_next_step_handler(message, question7)
    else:
        answers.append({6: catn(message.text)})
        bot.register_next_step_handler(message, question8)

def question8(message):
    bot.send_message(message.chat.id, eval(f'lang.part2_msg_{choosenlang}'))
    bot.send_message(message.chat.id, f'{questionlang} 8:\n{def_questions[8]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, f'{wronginput}')
        bot.register_next_step_handler(message, question8)
    else:
        answers.append({7: catn(message.text)})
        bot.register_next_step_handler(message, question9)

def question9(message):

    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    bot.send_message(message.chat.id, f'{questionlang} 9:\n{def_questions[9]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, f'{wronginput}')
        bot.register_next_step_handler(message, question9)
    else:
        answers.append({8: catn(message.text)})
        bot.register_next_step_handler(message, question10)

def question10(message):
    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    bot.send_message(message.chat.id, f'{questionlang} 10:\n{def_questions[10]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, f'{wronginput}')
        bot.register_next_step_handler(message, question10)
    else:
        answers.append({9: catn(message.text)})
        bot.register_next_step_handler(message, question11)

def question11(message):
    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    bot.send_message(message.chat.id, f'{questionlang} 11:\n{def_questions[11]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, f'{wronginput}')
        bot.register_next_step_handler(message, question11)
    else:
        answers.append({10: catn(message.text)})
        bot.register_next_step_handler(message, question12)

def question12(message):
    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    bot.send_message(message.chat.id, f'{questionlang} 12:\n{def_questions[12]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, f'{wronginput}')
        bot.register_next_step_handler(message, question12)
    else:
        answers.append({11: catn(message.text)})
        bot.register_next_step_handler(message, question13)

def question13(message):
    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    bot.send_message(message.chat.id, f'{questionlang} 13:\n{def_questions[13]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, f'{wronginput}')
        bot.register_next_step_handler(message, question13)
    else:
        answers.append({12: catn(message.text)})
        bot.register_next_step_handler(message, question14)

def question14(message):
    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    bot.send_message(message.chat.id, f'{questionlang} 14:\n{def_questions[14]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, f'{wronginput}')
        bot.register_next_step_handler(message, question14)
    else:
        answers.append({13: catn(message.text)})
        bot.register_next_step_handler(message, question15)

def question15(message):
    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    bot.send_message(message.chat.id, f'{questionlang} 15:\n{def_questions[15]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, f'{wronginput}')
        bot.register_next_step_handler(message, question15)
    else:
        answers.append({14: catn(message.text)})
        bot.register_next_step_handler(message, question16)

def question16(message):
    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    bot.send_message(message.chat.id, f'{questionlang} 16:\n{def_questions[16]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, f'{wronginput}')
        bot.register_next_step_handler(message, question16)
    else:
        answers.append({15: catn(message.text)})
        bot.register_next_step_handler(message, question17)

def question17(message):
    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    bot.send_message(message.chat.id, f'{questionlang} 17:\n{def_questions[17]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, f'{wronginput}')
        bot.register_next_step_handler(message, question17)
    else:
        answers.append({16: catn(message.text)})
        bot.register_next_step_handler(message, question18)

def question18(message):
    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    bot.send_message(message.chat.id, f'{questionlang} 18:\n{def_questions[18]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, f'{wronginput}')
        bot.register_next_step_handler(message, question18)
    else:
        answers.append({17: catn(message.text)})
        bot.register_next_step_handler(message, question19)

def question19(message):
    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    bot.send_message(message.chat.id, f'{questionlang} 19:\n{def_questions[19]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, f'{wronginput}')
        bot.register_next_step_handler(message, question19)
    else:
        answers.append({18: catn(message.text)})
        bot.register_next_step_handler(message, question20)

def question20(message):
    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    bot.send_message(message.chat.id, f'{questionlang} 20:\n{def_questions[20]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, f'{wronginput}')
        bot.register_next_step_handler(message, question20)
    else:
        answers.append({19: catn(message.text)})
        bot.register_next_step_handler(message, question21)

def question21(message):
    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    bot.send_message(message.chat.id, f'{questionlang} 21:\n{def_questions[21]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, f'{wronginput}')
        bot.register_next_step_handler(message, question21)
    else:
        answers.append({20: catn(message.text)})
        bot.register_next_step_handler(message, question22)

def question22(message):
    bot.send_message(message.chat.id, eval(f'lang.part3_msg_{choosenlang}'))
    bot.send_message(message.chat.id, f'{questionlang} 22:\n{def_questions[22]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, f'{wronginput}')
        bot.register_next_step_handler(message, question22)
    else:
        answers.append({21: catn(message.text)})
        bot.register_next_step_handler(message, question23)

def question23(message):
    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    bot.send_message(message.chat.id, f'{questionlang} 23:\n{def_questions[23]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, f'{wronginput}')
        bot.register_next_step_handler(message, question23)
    else:
        answers.append({22: catn(message.text)})
        bot.register_next_step_handler(message, question24)

def question24(message):
    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    bot.send_message(message.chat.id, f'{questionlang} 24:\n{def_questions[24]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, f'{wronginput}')
        bot.register_next_step_handler(message, question24)
    else:
        answers.append({23: catn(message.text)})
        bot.register_next_step_handler(message, question25)

def question25(message):
    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    bot.send_message(message.chat.id, f'{questionlang} 25:\n{def_questions[25]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, f'{wronginput}')
        bot.register_next_step_handler(message, question25)
    else:
        answers.append({24: catn(message.text)})
        bot.register_next_step_handler(message, question26)

def question26(message):
    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    bot.send_message(message.chat.id, f'{questionlang} 26:\n{def_questions[26]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, f'{wronginput}')
        bot.register_next_step_handler(message, question26)
    else:
        answers.append({25: catn(message.text)})
        bot.register_next_step_handler(message, question27)

def question27(message):
    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    bot.send_message(message.chat.id, f'{questionlang} 27:\n{def_questions[27]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, f'{wronginput}')
        bot.register_next_step_handler(message, question27)
    else:
        answers.append({26: catn(message.text)})
        bot.register_next_step_handler(message, question28)

def question28(message):
    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    bot.send_message(message.chat.id, f'{questionlang} 28:\n{def_questions[28]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, f'{wronginput}')
        bot.register_next_step_handler(message, question28)
    else:
        answers.append({27: catn(message.text)})
        bot.register_next_step_handler(message, question29)

def question29(message):
    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    bot.send_message(message.chat.id, f'{questionlang} 29:\n{def_questions[29]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, f'{wronginput}')
        bot.register_next_step_handler(message, question29)
    else:
        answers.append({28: catn(message.text)})
        bot.register_next_step_handler(message, question30)

def question30(message):
    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    bot.send_message(message.chat.id, f'{questionlang} 30:\n{def_questions[30]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, f'{wronginput}')
        bot.register_next_step_handler(message, question30)
    else:
        answers.append({29: catn(message.text)})
        bot.register_next_step_handler(message, question31)

def question31(message):
    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    bot.send_message(message.chat.id, f'{questionlang} 31:\n{def_questions[31]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, f'{wronginput}')
        bot.register_next_step_handler(message, question31)
    else:
        answers.append({30: catn(message.text)})
        bot.register_next_step_handler(message, question32)

def question32(message):
    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    bot.send_message(message.chat.id, f'{questionlang} 32:\n{def_questions[32]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, f'{wronginput}')
        bot.register_next_step_handler(message, question32)
    else:
        answers.append({31: catn(message.text)})
        bot.register_next_step_handler(message, question33)

def question33(message):
    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    bot.send_message(message.chat.id, f'{questionlang} 33:\n{def_questions[33]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, f'{wronginput}')
        bot.register_next_step_handler(message, question33)
    else:
        answers.append({32: catn(message.text)})
        bot.register_next_step_handler(message, question34)

def question34(message):
    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    bot.send_message(message.chat.id, f'{questionlang} 34:\n{def_questions[34]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, f'{wronginput}')
        bot.register_next_step_handler(message, question34)
    else:
        answers.append({33: catn(message.text)})
        bot.register_next_step_handler(message, question35)

def question35(message):
    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    bot.send_message(message.chat.id, f'{questionlang} 35:\n{def_questions[35]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, f'{wronginput}')
        bot.register_next_step_handler(message, question35)
    else:
        answers.append({34: catn(message.text)})
        bot.register_next_step_handler(message, question36)

def question36(message):
    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    bot.send_message(message.chat.id, f'{questionlang} 36:\n{def_questions[36]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, f'{wronginput}')
        bot.register_next_step_handler(message, question36)
    else:
        answers.append({35: catn(message.text)})
        bot.register_next_step_handler(message, question37)

def question37(message):
    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    bot.send_message(message.chat.id, f'{questionlang} 37:\n{def_questions[37]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, f'{wronginput}')
        bot.register_next_step_handler(message, question37)
    else:
        answers.append({36: catn(message.text)})
        bot.register_next_step_handler(message, question38)

def question38(message):
    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    bot.send_message(message.chat.id, f'{questionlang} 38:\n{def_questions[38]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, f'{wronginput}')
        bot.register_next_step_handler(message, question38)
    else:
        answers.append({37: catn(message.text)})
        bot.register_next_step_handler(message, question39)

def question39(message):
    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    bot.send_message(message.chat.id, f'{questionlang} 39:\n{def_questions[39]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, f'{wronginput}')
        bot.register_next_step_handler(message, question39)
    else:
        answers.append({38: catn(message.text)})
        bot.register_next_step_handler(message, question40)

def question40(message):
    bot.send_message(message.chat.id, eval(f'lang.part4_msg_{choosenlang}'))
    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    bot.send_message(message.chat.id, f'{questionlang} 40:\n{def_questions[40]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, f'{wronginput}')
        bot.register_next_step_handler(message, question40)
    else:
        answers.append({39: catn(message.text)})
        bot.register_next_step_handler(message, question41)

def question41(message):
    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    bot.send_message(message.chat.id, f'{questionlang} 41:\n{def_questions[41]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, f'{wronginput}')
        bot.register_next_step_handler(message, question41)
    else:
        answers.append({40: catn(message.text)})
        bot.register_next_step_handler(message, question42)
    
def question42(message):
    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    bot.send_message(message.chat.id, f'{questionlang} 42:\n{def_questions[42]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, f'{wronginput}')
        bot.register_next_step_handler(message, question42)
    else:
        answers.append({41: catn(message.text)})
        bot.register_next_step_handler(message, question43)

def question43(message):
    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    bot.send_message(message.chat.id, f'{questionlang} 43:\n{def_questions[43]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, f'{wronginput}')
        bot.register_next_step_handler(message, question43)
    else:
        answers.append({42: catn(message.text)})
        bot.register_next_step_handler(message, question44)

def question44(message):
    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    bot.send_message(message.chat.id, f'{questionlang} 44:\n{def_questions[44]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, f'{wronginput}')
        bot.register_next_step_handler(message, question44)
    else:
        answers.append({43: catn(message.text)})
        bot.register_next_step_handler(message, question45)

def question45(message):
    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    bot.send_message(message.chat.id, f'{questionlang} 45:\n{def_questions[45]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, f'{wronginput}')
        bot.register_next_step_handler(message, question45)
    else:
        answers.append({44: catn(message.text)})
        bot.register_next_step_handler(message, question46)

def question46(message):
    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    bot.send_message(message.chat.id, f'{questionlang} 46:\n{def_questions[46]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, f'{wronginput}')
        bot.register_next_step_handler(message, question46)
    else:
        answers.append({45: catn(message.text)})
        bot.register_next_step_handler(message, question47)

def question47(message):
    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    bot.send_message(message.chat.id, f'{questionlang} 47:\n{def_questions[47]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, f'{wronginput}')
        bot.register_next_step_handler(message, question47)
    else:
        answers.append({46: catn(message.text)})
        bot.register_next_step_handler(message, question48)

def question48(message):
    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    bot.send_message(message.chat.id, f'{questionlang} 48:\n{def_questions[48]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, f'{wronginput}')
        bot.register_next_step_handler(message, question48)
    else:
        answers.append({47: catn(message.text)})
        bot.register_next_step_handler(message, question49)

def question49(message):
    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    bot.send_message(message.chat.id, f'{questionlang} 49:\n{def_questions[49]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, f'{wronginput}')
        bot.register_next_step_handler(message, question49)
    else:
        answers.append({48: catn(message.text)})
        bot.register_next_step_handler(message, question50)

def question50(message):
    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    bot.send_message(message.chat.id, f'{questionlang} 50:\n{def_questions[50]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, f'{wronginput}')
        bot.register_next_step_handler(message, question50)
    else:
        answers.append({49: catn(message.text)})
        bot.register_next_step_handler(message, question51)

def question51(message):
    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    bot.send_message(message.chat.id, f'{questionlang} 51:\n{def_questions[51]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, f'{wronginput}')
        bot.register_next_step_handler(message, question51)
    else:
        answers.append({50: catn(message.text)})
        bot.register_next_step_handler(message, question52)

def question52(message):
    bot.send_message(message.chat.id, eval(f'lang.part5_msg_{choosenlang}'))
    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    bot.send_message(message.chat.id, f'{questionlang} 52:\n{def_questions[52]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, f'{wronginput}')
        bot.register_next_step_handler(message, question52)
    else:
        answers.append({51: catn(message.text)})
        bot.register_next_step_handler(message, question53)

def question53(message):
    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    bot.send_message(message.chat.id, f'{questionlang} 53:\n{def_questions[53]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, f'{wronginput}')
        bot.register_next_step_handler(message, question53)
    else:
        answers.append({52: catn(message.text)})
        bot.register_next_step_handler(message, question54)

def question54(message):
    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    bot.send_message(message.chat.id, f'{questionlang} 54:\n{def_questions[54]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, f'{wronginput}')
        bot.register_next_step_handler(message, question54)
    else:
        answers.append({53: catn(message.text)})
        bot.register_next_step_handler(message, question55)

def question55(message):
    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    bot.send_message(message.chat.id, f'{questionlang} 55:\n{def_questions[55]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, f'{wronginput}')
        bot.register_next_step_handler(message, question55)
    else:
        answers.append({54: catn(message.text)})
        bot.register_next_step_handler(message, question56)

def question56(message):
    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    bot.send_message(message.chat.id, f'{questionlang} 56:\n{def_questions[56]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, f'{wronginput}')
        bot.register_next_step_handler(message, question56)
    else:
        answers.append({55: catn(message.text)})
        bot.register_next_step_handler(message, question57)

def question57(message):
    bot.send_message(message.chat.id, eval(f'lang.part6_msg_{choosenlang}'))
    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    bot.send_message(message.chat.id, f'{questionlang} 57:\n{def_questions[57]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, f'{wronginput}')
        bot.register_next_step_handler(message, question57)
    else:
        answers.append({56: catn(message.text)})
        bot.register_next_step_handler(message, question58)

def question58(message):
    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    bot.send_message(message.chat.id, f'{questionlang} 58:\n{def_questions[58]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, f'{wronginput}')
        bot.register_next_step_handler(message, question58)
    else:
        answers.append({57: catn(message.text)})
        bot.register_next_step_handler(message, question59)

def question59(message):
    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    bot.send_message(message.chat.id, f'{questionlang} 59:\n{def_questions[59]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, f'{wronginput}')
        bot.register_next_step_handler(message, question59)
    else:
        answers.append({58: catn(message.text)})
        bot.register_next_step_handler(message, question60)

def question60(message):
    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    bot.send_message(message.chat.id, f'{questionlang} 60:\n{def_questions[60]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, f'{wronginput}')
        bot.register_next_step_handler(message, question60)
    else:
        answers.append({59: catn(message.text)})
        bot.register_next_step_handler(message, question61)

def question61(message):
    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    bot.send_message(message.chat.id, f'{questionlang} 61:\n{def_questions[61]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, f'{wronginput}')
        bot.register_next_step_handler(message, question61)
    else:
        answers.append({60: catn(message.text)})
        bot.register_next_step_handler(message, question62)

def question62(message):
    bot.send_message(message.chat.id, eval(f'lang.lastq_msg_{choosenlang}'))
    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    bot.send_message(message.chat.id, f'{questionlang} 62:\n{def_questions[62]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, f'{wronginput}')
        bot.register_next_step_handler(message, question62)
    else:
        answers.append({61: catn(message.text)})
        bot.register_next_step_handler(message, finish)


def finish(message):
    # bot.send_message(message.chat.id, f"Your answer: {message.text}")
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, f'{wronginput}')
        bot.register_next_step_handler(message, finish)
    else:
        answers.append({62: catn(message.text)})
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=1)
        markup.add(eval(f'lang.restart_btn_{choosenlang}'))
        wait = bot.send_message(message.chat.id, eval(f'lang.wait_msg_{choosenlang}'))
        wait
        name = message.from_user.first_name
        pcresults = pwp.results(pwp.format_answers(answers=answers))
        url = f'https://www.politicalcompass.org/analysis2?{pcresults}'
        image = f'https://www.politicalcompass.org/chart?{pcresults}'
        pdf = f'https://www.politicalcompass.org/pdfcertificate?pname={name}&{pcresults}'
        linkmsg = eval(f'lang.link_msg_{choosenlang}')
        bot.delete_message(message.chat.id, wait.message_id)
        bot.send_message(message.chat.id, eval(f'lang.urpc_msg_{choosenlang}'))
        bot.send_message(message.chat.id, f'{elr} \n{pcresults.split("ec=")[1].split("&")[0]}\n{sla} \n{pcresults.split("soc=")[1]}')
        bot.send_photo(message.chat.id, image, caption=eval(f'lang.chart_msg_{choosenlang}')) 
        bot.send_document(message.chat.id, pdf , caption=eval(f'lang.pdf_msg_{choosenlang}'))
        bot.send_message(message.chat.id, f'{url}\n{linkmsg}')
        bot.send_message(message.chat.id, eval(f'lang.tnks_msg_{choosenlang}'), reply_markup=markup)
