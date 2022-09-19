import sys
import telebot
from telebot import types

import language as lang
from config import token
import politicwebspost as pwp
from helper import database as db

bot = telebot.TeleBot(token)


def helpcommand(choosenlang):
    help_ = eval(f'lang.helpcommand_{choosenlang}')
    return help_
def startcommand(choosenlang):
    start_ = eval(f'lang.startcommand_{choosenlang}')
    return start_
def cancelcommand(choosenlang):
    cancel_ = eval(f'lang.cancelcommand_{choosenlang}')
    return cancel_
def langcommand(choosenlang):
    lang_ = eval(f'lang.langcommand_{choosenlang}')
    return lang_
def resultcommand(choosenlang):
    result_ = eval(f'lang.resultcommand_{choosenlang}')
    return result_
def renamecommand(choosenlang):
    rename_ = eval(f'lang.renamecommand_{choosenlang}')
    return rename_

bot.delete_my_commands()

bot.set_my_commands(
    commands=[
        telebot.types.BotCommand('/start', startcommand('en')),
        telebot.types.BotCommand('/help', helpcommand('en')),
        telebot.types.BotCommand('/cancel', cancelcommand('en')),
        telebot.types.BotCommand('/lang', langcommand('en')),
        telebot.types.BotCommand('/myresult', resultcommand('en')),
        telebot.types.BotCommand('/rename', renamecommand('en')),
        ])


def catn(replay, userid):
    choosenlang = db.userlanguage(userid)
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

def rkm(userid):
    choosenlang = db.userlanguage(userid)
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
    choosenlang = db.userlanguage(message.chat.id)
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('🇬🇧 English', callback_data='en'))
    markup.add(types.InlineKeyboardButton('العربية 🇸🇦', callback_data='ar'))
    markup.add(types.InlineKeyboardButton('دّاريجة 🇲🇦', callback_data='ary'))
    bot.send_message(message.chat.id,eval(f'lang.chooselang_{choosenlang}'), reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'en')
def change_to_en(call: types.CallbackQuery):
    db.changeuserlang(call.from_user.id, 'en')
    bot.delete_message(call.message.chat.id, call.message.message_id)
    rebuild_buttons(call.message.chat.id)

@bot.callback_query_handler(func=lambda call: call.data == 'ar')
def change_to_en(call: types.CallbackQuery):
    db.changeuserlang(call.from_user.id, 'ar')
    bot.delete_message(call.message.chat.id, call.message.message_id)
    rebuild_buttons(call.message.chat.id)

@bot.callback_query_handler(func=lambda call: call.data == 'ary')
def change_to_en(call: types.CallbackQuery):
    db.changeuserlang(call.from_user.id, 'ary')
    bot.delete_message(call.message.chat.id, call.message.message_id)
    rebuild_buttons(call.message.chat.id)

@bot.message_handler(commands=['help'])
def help_message(message):
    global choosenlang
    choosenlang = db.userlanguage(message.from_user.id)
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=1)
    markup.add(eval(f'lang.start_btn_{choosenlang}'))
    bot.send_message(message.chat.id,eval(f'lang.help_msg_{choosenlang}') , reply_markup=markup)


def rebuild_buttons(userid):
    global choosenlang
    choosenlang = db.userlanguage(userid)
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=1)
    markup.add(eval(f'lang.start_btn_{choosenlang}'))
    bot.send_message(userid, eval(f'lang.langchanged_{choosenlang}') , reply_markup=markup)

@bot.message_handler(commands=['cancel'])
def cancel_message(message):
    global choosenlang
    choosenlang = db.userlanguage(message.from_user.id)
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=1)
    markup.add(eval(f'lang.start_btn_{choosenlang}'))
    bot.send_message(message.chat.id, eval(f'lang.canceled_{choosenlang}'), reply_markup=markup)

@bot.message_handler(commands=['start'])
def start_message(message):
    if db.usercheck(message.chat.id) == False:
        db.add_user(message.chat.id, message.chat.first_name, message.chat.username, 'en', 'None')
        language_bot(message)
    else:
        global choosenlang
        choosenlang = db.userlanguage(message.from_user.id)
        bot.reply_to(message, eval(f'lang.starting_msg_{choosenlang}'))
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=False)
        markup.add(eval(f'lang.letsgo_btn_{choosenlang}'))
        bot.send_message(message.chat.id, eval(f'lang.ready_msg_{choosenlang}'), reply_markup=markup)
        bot.register_next_step_handler(message, question1)

    


def defquestions_(userid):
    choosenlang = db.userlanguage(userid)
    def_questions = eval(f'lang.def_questions_{choosenlang}')
    return def_questions
def func_questionlang(userid):
    choosenlang = db.userlanguage(userid)
    questionlang_ = eval(f'lang.question_{choosenlang}')
    return questionlang_
def func_wronginput(userid):
    choosenlang = db.userlanguage(userid)
    wronginput_ = eval(f'lang.wronginput_{choosenlang}')
    return wronginput_
def func_elr(userid):
    choosenlang = db.userlanguage(userid)
    elr_ = eval(f'lang.elr_msg_{choosenlang}')
    return elr_
def func_sla(userid):
    choosenlang = db.userlanguage(userid)
    sla_ = eval(f'lang.sla_msg_{choosenlang}')
    return sla_

@bot.message_handler(func=lambda message: True)
def messagess(message):
    userid = message.from_user.id
    choosenlang = db.userlanguage(userid)
    if message.text == eval(f'lang.restart_btn_{choosenlang}') or message.text == eval(f'lang.start_btn_{choosenlang}'):
        start_message(message)
    else:
        bot.reply_to(message, eval(f'lang.needhelp_msg_{choosenlang}'))

def question1(message):
    choosenlang = db.userlanguage(message.from_user.id)
    if message.text.startswith('/'):
        cancel_message(message)
    else:    
        bot.send_message(message.chat.id, eval(f'lang.journeycancel_msg_{choosenlang}'))
        bot.send_message(message.chat.id, eval(f'lang.part1_msg_{choosenlang}'))
        bot.send_message(message.chat.id, f'{func_questionlang(message.from_user.id)} 1:\n{defquestions_(message.from_user.id)[1]}', reply_markup=rkm(message.from_user.id))
        bot.register_next_step_handler(message, question2)
    
def question2(message):
    choosenlang = db.userlanguage(message.from_user.id)
    if message.text == '/cancel':
        cancel_message(message)
    else:
        bot.send_message(message.chat.id, f'{func_questionlang(message.from_user.id)} 2:\n{defquestions_(message.from_user.id)[2]}', reply_markup=rkm(message.from_user.id))
        if catn(message.text, message.from_user.id) == 'error':
            bot.send_message(message.chat.id, f'{func_wronginput(message.from_user.id)}')
            bot.register_next_step_handler(message, question2)
        else:
            db.insert_answers(message.from_user.id, catn(message.text, message.from_user.id), '1')
            bot.register_next_step_handler(message, question3)

def question3(message):
    
    if message.text == '/cancel':
        cancel_message(message)
    else:
        bot.send_message(message.chat.id, f'{func_questionlang(message.from_user.id)} 3:\n{defquestions_(message.from_user.id)[3]}', reply_markup=rkm(message.from_user.id))
        if catn(message.text, message.from_user.id) == 'error':
            bot.send_message(message.chat.id, f'{func_wronginput(message.from_user.id)}')
            bot.register_next_step_handler(message, question3)
        else:
            db.insert_answers(message.from_user.id, catn(message.text, message.from_user.id), '2')
            bot.register_next_step_handler(message, question4)

def question4(message):
    if message.text == '/cancel':
        cancel_message(message)
    else:
        
        bot.send_message(message.chat.id, f'{func_questionlang(message.from_user.id)} 4:\n{defquestions_(message.from_user.id)[4]}', reply_markup=rkm(message.from_user.id))
        if catn(message.text, message.from_user.id) == 'error':
            bot.send_message(message.chat.id, f'{func_wronginput(message.from_user.id)}')
            bot.register_next_step_handler(message, question4)
        else:
            db.insert_answers(message.from_user.id, catn(message.text, message.from_user.id), '3')
            bot.register_next_step_handler(message, question5)

def question5(message):
    if message.text == '/cancel':
        cancel_message(message)
    else:
        
        bot.send_message(message.chat.id, f'{func_questionlang(message.from_user.id)} 5:\n{defquestions_(message.from_user.id)[5]}', reply_markup=rkm(message.from_user.id))
        if catn(message.text, message.from_user.id) == 'error':
            bot.send_message(message.chat.id, f'{func_wronginput(message.from_user.id)}')
            bot.register_next_step_handler(message, question5)
        else:
            db.insert_answers(message.from_user.id, catn(message.text, message.from_user.id), '4')
            bot.register_next_step_handler(message, question6)

def question6(message):
    if message.text == '/cancel':
        cancel_message(message)
    else:
        
        bot.send_message(message.chat.id, f'{func_questionlang(message.from_user.id)} 6:\n{defquestions_(message.from_user.id)[6]}', reply_markup=rkm(message.from_user.id))
        if catn(message.text, message.from_user.id) == 'error':
            bot.send_message(message.chat.id, f'{func_wronginput(message.from_user.id)}')
            bot.register_next_step_handler(message, question6)
        else:
            db.insert_answers(message.from_user.id, catn(message.text, message.from_user.id), '5')
            bot.register_next_step_handler(message, question7)

def question7(message):
    if message.text == '/cancel':
        cancel_message(message)
    else:    
        
        bot.send_message(message.chat.id, f'{func_questionlang(message.from_user.id)} 7:\n{defquestions_(message.from_user.id)[7]}', reply_markup=rkm(message.from_user.id))
        if catn(message.text, message.from_user.id) == 'error':
            bot.send_message(message.chat.id, f'{func_wronginput(message.from_user.id)}')
            bot.register_next_step_handler(message, question7)
        else:
            db.insert_answers(message.from_user.id, catn(message.text, message.from_user.id), '6')
            bot.register_next_step_handler(message, question8)

def question8(message):
    bot.send_message(message.chat.id, eval(f'lang.part2_msg_{choosenlang}'))
    bot.send_message(message.chat.id, f'{func_questionlang(message.from_user.id)} 8:\n{defquestions_(message.from_user.id)[8]}', reply_markup=rkm(message.from_user.id))
    if catn(message.text, message.from_user.id) == 'error':
        bot.send_message(message.chat.id, f'{func_wronginput(message.from_user.id)}')
        bot.register_next_step_handler(message, question8)
    else:
        db.insert_answers(message.from_user.id, catn(message.text, message.from_user.id), '7')
        bot.register_next_step_handler(message, question9)

def question9(message):

    
    bot.send_message(message.chat.id, f'{func_questionlang(message.from_user.id)} 9:\n{defquestions_(message.from_user.id)[9]}', reply_markup=rkm(message.from_user.id))
    if catn(message.text, message.from_user.id) == 'error':
        bot.send_message(message.chat.id, f'{func_wronginput(message.from_user.id)}')
        bot.register_next_step_handler(message, question9)
    else:
        db.insert_answers(message.from_user.id, catn(message.text, message.from_user.id), '8')
        bot.register_next_step_handler(message, question10)

def question10(message):
    
    bot.send_message(message.chat.id, f'{func_questionlang(message.from_user.id)} 10:\n{defquestions_(message.from_user.id)[10]}', reply_markup=rkm(message.from_user.id))
    if catn(message.text, message.from_user.id) == 'error':
        bot.send_message(message.chat.id, f'{func_wronginput(message.from_user.id)}')
        bot.register_next_step_handler(message, question10)
    else:
        db.insert_answers(message.from_user.id, catn(message.text, message.from_user.id), '9')
        bot.register_next_step_handler(message, question11)

def question11(message):
    
    bot.send_message(message.chat.id, f'{func_questionlang(message.from_user.id)} 11:\n{defquestions_(message.from_user.id)[11]}', reply_markup=rkm(message.from_user.id))
    if catn(message.text, message.from_user.id) == 'error':
        bot.send_message(message.chat.id, f'{func_wronginput(message.from_user.id)}')
        bot.register_next_step_handler(message, question11)
    else:
        db.insert_answers(message.from_user.id, catn(message.text, message.from_user.id), '10')
        bot.register_next_step_handler(message, question12)

def question12(message):
    
    bot.send_message(message.chat.id, f'{func_questionlang(message.from_user.id)} 12:\n{defquestions_(message.from_user.id)[12]}', reply_markup=rkm(message.from_user.id))
    if catn(message.text, message.from_user.id) == 'error':
        bot.send_message(message.chat.id, f'{func_wronginput(message.from_user.id)}')
        bot.register_next_step_handler(message, question12)
    else:
        db.insert_answers(message.from_user.id, catn(message.text, message.from_user.id), '11')
        bot.register_next_step_handler(message, question13)

def question13(message):
    
    bot.send_message(message.chat.id, f'{func_questionlang(message.from_user.id)} 13:\n{defquestions_(message.from_user.id)[13]}', reply_markup=rkm(message.from_user.id))
    if catn(message.text, message.from_user.id) == 'error':
        bot.send_message(message.chat.id, f'{func_wronginput(message.from_user.id)}')
        bot.register_next_step_handler(message, question13)
    else:
        db.insert_answers(message.from_user.id, catn(message.text, message.from_user.id), '12')
        bot.register_next_step_handler(message, question14)

def question14(message):
    
    bot.send_message(message.chat.id, f'{func_questionlang(message.from_user.id)} 14:\n{defquestions_(message.from_user.id)[14]}', reply_markup=rkm(message.from_user.id))
    if catn(message.text, message.from_user.id) == 'error':
        bot.send_message(message.chat.id, f'{func_wronginput(message.from_user.id)}')
        bot.register_next_step_handler(message, question14)
    else:
        db.insert_answers(message.from_user.id, catn(message.text, message.from_user.id), '13')
        bot.register_next_step_handler(message, question15)

def question15(message):
    
    bot.send_message(message.chat.id, f'{func_questionlang(message.from_user.id)} 15:\n{defquestions_(message.from_user.id)[15]}', reply_markup=rkm(message.from_user.id))
    if catn(message.text, message.from_user.id) == 'error':
        bot.send_message(message.chat.id, f'{func_wronginput(message.from_user.id)}')
        bot.register_next_step_handler(message, question15)
    else:
        db.insert_answers(message.from_user.id, catn(message.text, message.from_user.id), '14')
        bot.register_next_step_handler(message, question16)

def question16(message):
    
    bot.send_message(message.chat.id, f'{func_questionlang(message.from_user.id)} 16:\n{defquestions_(message.from_user.id)[16]}', reply_markup=rkm(message.from_user.id))
    if catn(message.text, message.from_user.id) == 'error':
        bot.send_message(message.chat.id, f'{func_wronginput(message.from_user.id)}')
        bot.register_next_step_handler(message, question16)
    else:
        db.insert_answers(message.from_user.id, catn(message.text, message.from_user.id), '15')
        bot.register_next_step_handler(message, question17)

def question17(message):
    
    bot.send_message(message.chat.id, f'{func_questionlang(message.from_user.id)} 17:\n{defquestions_(message.from_user.id)[17]}', reply_markup=rkm(message.from_user.id))
    if catn(message.text, message.from_user.id) == 'error':
        bot.send_message(message.chat.id, f'{func_wronginput(message.from_user.id)}')
        bot.register_next_step_handler(message, question17)
    else:
        db.insert_answers(message.from_user.id, catn(message.text, message.from_user.id), '16')
        bot.register_next_step_handler(message, question18)

def question18(message):
    
    bot.send_message(message.chat.id, f'{func_questionlang(message.from_user.id)} 18:\n{defquestions_(message.from_user.id)[18]}', reply_markup=rkm(message.from_user.id))
    if catn(message.text, message.from_user.id) == 'error':
        bot.send_message(message.chat.id, f'{func_wronginput(message.from_user.id)}')
        bot.register_next_step_handler(message, question18)
    else:
        db.insert_answers(message.from_user.id, catn(message.text, message.from_user.id), '17')
        bot.register_next_step_handler(message, question19)

def question19(message):
    
    bot.send_message(message.chat.id, f'{func_questionlang(message.from_user.id)} 19:\n{defquestions_(message.from_user.id)[19]}', reply_markup=rkm(message.from_user.id))
    if catn(message.text, message.from_user.id) == 'error':
        bot.send_message(message.chat.id, f'{func_wronginput(message.from_user.id)}')
        bot.register_next_step_handler(message, question19)
    else:
        db.insert_answers(message.from_user.id, catn(message.text, message.from_user.id), '18')
        bot.register_next_step_handler(message, question20)

def question20(message):
    
    bot.send_message(message.chat.id, f'{func_questionlang(message.from_user.id)} 20:\n{defquestions_(message.from_user.id)[20]}', reply_markup=rkm(message.from_user.id))
    if catn(message.text, message.from_user.id) == 'error':
        bot.send_message(message.chat.id, f'{func_wronginput(message.from_user.id)}')
        bot.register_next_step_handler(message, question20)
    else:
        db.insert_answers(message.from_user.id, catn(message.text, message.from_user.id), '19')
        bot.register_next_step_handler(message, question21)

def question21(message):
    
    bot.send_message(message.chat.id, f'{func_questionlang(message.from_user.id)} 21:\n{defquestions_(message.from_user.id)[21]}', reply_markup=rkm(message.from_user.id))
    if catn(message.text, message.from_user.id) == 'error':
        bot.send_message(message.chat.id, f'{func_wronginput(message.from_user.id)}')
        bot.register_next_step_handler(message, question21)
    else:
        db.insert_answers(message.from_user.id, catn(message.text, message.from_user.id), '20')
        bot.register_next_step_handler(message, question22)

def question22(message):
    bot.send_message(message.chat.id, eval(f'lang.part3_msg_{choosenlang}'))
    bot.send_message(message.chat.id, f'{func_questionlang(message.from_user.id)} 22:\n{defquestions_(message.from_user.id)[22]}', reply_markup=rkm(message.from_user.id))
    if catn(message.text, message.from_user.id) == 'error':
        bot.send_message(message.chat.id, f'{func_wronginput(message.from_user.id)}')
        bot.register_next_step_handler(message, question22)
    else:
        db.insert_answers(message.from_user.id, catn(message.text, message.from_user.id), '21')
        bot.register_next_step_handler(message, question23)

def question23(message):
    
    bot.send_message(message.chat.id, f'{func_questionlang(message.from_user.id)} 23:\n{defquestions_(message.from_user.id)[23]}', reply_markup=rkm(message.from_user.id))
    if catn(message.text, message.from_user.id) == 'error':
        bot.send_message(message.chat.id, f'{func_wronginput(message.from_user.id)}')
        bot.register_next_step_handler(message, question23)
    else:
        db.insert_answers(message.from_user.id, catn(message.text, message.from_user.id), '22')
        bot.register_next_step_handler(message, question24)

def question24(message):
    
    bot.send_message(message.chat.id, f'{func_questionlang(message.from_user.id)} 24:\n{defquestions_(message.from_user.id)[24]}', reply_markup=rkm(message.from_user.id))
    if catn(message.text, message.from_user.id) == 'error':
        bot.send_message(message.chat.id, f'{func_wronginput(message.from_user.id)}')
        bot.register_next_step_handler(message, question24)
    else:
        db.insert_answers(message.from_user.id, catn(message.text, message.from_user.id), '23')
        bot.register_next_step_handler(message, question25)

def question25(message):
    
    bot.send_message(message.chat.id, f'{func_questionlang(message.from_user.id)} 25:\n{defquestions_(message.from_user.id)[25]}', reply_markup=rkm(message.from_user.id))
    if catn(message.text, message.from_user.id) == 'error':
        bot.send_message(message.chat.id, f'{func_wronginput(message.from_user.id)}')
        bot.register_next_step_handler(message, question25)
    else:
        db.insert_answers(message.from_user.id, catn(message.text, message.from_user.id), '24')
        bot.register_next_step_handler(message, question26)

def question26(message):
    
    bot.send_message(message.chat.id, f'{func_questionlang(message.from_user.id)} 26:\n{defquestions_(message.from_user.id)[26]}', reply_markup=rkm(message.from_user.id))
    if catn(message.text, message.from_user.id) == 'error':
        bot.send_message(message.chat.id, f'{func_wronginput(message.from_user.id)}')
        bot.register_next_step_handler(message, question26)
    else:
        db.insert_answers(message.from_user.id, catn(message.text, message.from_user.id), '25')
        bot.register_next_step_handler(message, question27)

def question27(message):
    
    bot.send_message(message.chat.id, f'{func_questionlang(message.from_user.id)} 27:\n{defquestions_(message.from_user.id)[27]}', reply_markup=rkm(message.from_user.id))
    if catn(message.text, message.from_user.id) == 'error':
        bot.send_message(message.chat.id, f'{func_wronginput(message.from_user.id)}')
        bot.register_next_step_handler(message, question27)
    else:
        db.insert_answers(message.from_user.id, catn(message.text, message.from_user.id), '26')
        bot.register_next_step_handler(message, question28)

def question28(message):
    
    bot.send_message(message.chat.id, f'{func_questionlang(message.from_user.id)} 28:\n{defquestions_(message.from_user.id)[28]}', reply_markup=rkm(message.from_user.id))
    if catn(message.text, message.from_user.id) == 'error':
        bot.send_message(message.chat.id, f'{func_wronginput(message.from_user.id)}')
        bot.register_next_step_handler(message, question28)
    else:
        db.insert_answers(message.from_user.id, catn(message.text, message.from_user.id), '27')
        bot.register_next_step_handler(message, question29)

def question29(message):
    
    bot.send_message(message.chat.id, f'{func_questionlang(message.from_user.id)} 29:\n{defquestions_(message.from_user.id)[29]}', reply_markup=rkm(message.from_user.id))
    if catn(message.text, message.from_user.id) == 'error':
        bot.send_message(message.chat.id, f'{func_wronginput(message.from_user.id)}')
        bot.register_next_step_handler(message, question29)
    else:
        db.insert_answers(message.from_user.id, catn(message.text, message.from_user.id), '28')
        bot.register_next_step_handler(message, question30)

def question30(message):
    
    bot.send_message(message.chat.id, f'{func_questionlang(message.from_user.id)} 30:\n{defquestions_(message.from_user.id)[30]}', reply_markup=rkm(message.from_user.id))
    if catn(message.text, message.from_user.id) == 'error':
        bot.send_message(message.chat.id, f'{func_wronginput(message.from_user.id)}')
        bot.register_next_step_handler(message, question30)
    else:
        db.insert_answers(message.from_user.id, catn(message.text, message.from_user.id), '29')
        bot.register_next_step_handler(message, question31)

def question31(message):
    
    bot.send_message(message.chat.id, f'{func_questionlang(message.from_user.id)} 31:\n{defquestions_(message.from_user.id)[31]}', reply_markup=rkm(message.from_user.id))
    if catn(message.text, message.from_user.id) == 'error':
        bot.send_message(message.chat.id, f'{func_wronginput(message.from_user.id)}')
        bot.register_next_step_handler(message, question31)
    else:
        db.insert_answers(message.from_user.id, catn(message.text, message.from_user.id), '30')
        bot.register_next_step_handler(message, question32)

def question32(message):
    
    bot.send_message(message.chat.id, f'{func_questionlang(message.from_user.id)} 32:\n{defquestions_(message.from_user.id)[32]}', reply_markup=rkm(message.from_user.id))
    if catn(message.text, message.from_user.id) == 'error':
        bot.send_message(message.chat.id, f'{func_wronginput(message.from_user.id)}')
        bot.register_next_step_handler(message, question32)
    else:
        db.insert_answers(message.from_user.id, catn(message.text, message.from_user.id), '31')
        bot.register_next_step_handler(message, question33)

def question33(message):
    
    bot.send_message(message.chat.id, f'{func_questionlang(message.from_user.id)} 33:\n{defquestions_(message.from_user.id)[33]}', reply_markup=rkm(message.from_user.id))
    if catn(message.text, message.from_user.id) == 'error':
        bot.send_message(message.chat.id, f'{func_wronginput(message.from_user.id)}')
        bot.register_next_step_handler(message, question33)
    else:
        db.insert_answers(message.from_user.id, catn(message.text, message.from_user.id), '32')
        bot.register_next_step_handler(message, question34)

def question34(message):
    
    bot.send_message(message.chat.id, f'{func_questionlang(message.from_user.id)} 34:\n{defquestions_(message.from_user.id)[34]}', reply_markup=rkm(message.from_user.id))
    if catn(message.text, message.from_user.id) == 'error':
        bot.send_message(message.chat.id, f'{func_wronginput(message.from_user.id)}')
        bot.register_next_step_handler(message, question34)
    else:
        db.insert_answers(message.from_user.id, catn(message.text, message.from_user.id), '33')
        bot.register_next_step_handler(message, question35)

def question35(message):
    
    bot.send_message(message.chat.id, f'{func_questionlang(message.from_user.id)} 35:\n{defquestions_(message.from_user.id)[35]}', reply_markup=rkm(message.from_user.id))
    if catn(message.text, message.from_user.id) == 'error':
        bot.send_message(message.chat.id, f'{func_wronginput(message.from_user.id)}')
        bot.register_next_step_handler(message, question35)
    else:
        db.insert_answers(message.from_user.id, catn(message.text, message.from_user.id), '34')
        bot.register_next_step_handler(message, question36)

def question36(message):
    
    bot.send_message(message.chat.id, f'{func_questionlang(message.from_user.id)} 36:\n{defquestions_(message.from_user.id)[36]}', reply_markup=rkm(message.from_user.id))
    if catn(message.text, message.from_user.id) == 'error':
        bot.send_message(message.chat.id, f'{func_wronginput(message.from_user.id)}')
        bot.register_next_step_handler(message, question36)
    else:
        db.insert_answers(message.from_user.id, catn(message.text, message.from_user.id), '35')
        bot.register_next_step_handler(message, question37)

def question37(message):
    
    bot.send_message(message.chat.id, f'{func_questionlang(message.from_user.id)} 37:\n{defquestions_(message.from_user.id)[37]}', reply_markup=rkm(message.from_user.id))
    if catn(message.text, message.from_user.id) == 'error':
        bot.send_message(message.chat.id, f'{func_wronginput(message.from_user.id)}')
        bot.register_next_step_handler(message, question37)
    else:
        db.insert_answers(message.from_user.id, catn(message.text, message.from_user.id), '36')
        bot.register_next_step_handler(message, question38)

def question38(message):
    
    bot.send_message(message.chat.id, f'{func_questionlang(message.from_user.id)} 38:\n{defquestions_(message.from_user.id)[38]}', reply_markup=rkm(message.from_user.id))
    if catn(message.text, message.from_user.id) == 'error':
        bot.send_message(message.chat.id, f'{func_wronginput(message.from_user.id)}')
        bot.register_next_step_handler(message, question38)
    else:
        db.insert_answers(message.from_user.id, catn(message.text, message.from_user.id), '37')
        bot.register_next_step_handler(message, question39)

def question39(message):
    
    bot.send_message(message.chat.id, f'{func_questionlang(message.from_user.id)} 39:\n{defquestions_(message.from_user.id)[39]}', reply_markup=rkm(message.from_user.id))
    if catn(message.text, message.from_user.id) == 'error':
        bot.send_message(message.chat.id, f'{func_wronginput(message.from_user.id)}')
        bot.register_next_step_handler(message, question39)
    else:
        db.insert_answers(message.from_user.id, catn(message.text, message.from_user.id), '38')
        bot.register_next_step_handler(message, question40)

def question40(message):
    bot.send_message(message.chat.id, eval(f'lang.part4_msg_{choosenlang}'))
    
    bot.send_message(message.chat.id, f'{func_questionlang(message.from_user.id)} 40:\n{defquestions_(message.from_user.id)[40]}', reply_markup=rkm(message.from_user.id))
    if catn(message.text, message.from_user.id) == 'error':
        bot.send_message(message.chat.id, f'{func_wronginput(message.from_user.id)}')
        bot.register_next_step_handler(message, question40)
    else:
        db.insert_answers(message.from_user.id, catn(message.text, message.from_user.id), '39')
        bot.register_next_step_handler(message, question41)

def question41(message):
    
    bot.send_message(message.chat.id, f'{func_questionlang(message.from_user.id)} 41:\n{defquestions_(message.from_user.id)[41]}', reply_markup=rkm(message.from_user.id))
    if catn(message.text, message.from_user.id) == 'error':
        bot.send_message(message.chat.id, f'{func_wronginput(message.from_user.id)}')
        bot.register_next_step_handler(message, question41)
    else:
        db.insert_answers(message.from_user.id, catn(message.text, message.from_user.id), '40')
        bot.register_next_step_handler(message, question42)
    
def question42(message):
    
    bot.send_message(message.chat.id, f'{func_questionlang(message.from_user.id)} 42:\n{defquestions_(message.from_user.id)[42]}', reply_markup=rkm(message.from_user.id))
    if catn(message.text, message.from_user.id) == 'error':
        bot.send_message(message.chat.id, f'{func_wronginput(message.from_user.id)}')
        bot.register_next_step_handler(message, question42)
    else:
        db.insert_answers(message.from_user.id, catn(message.text, message.from_user.id), '41')
        bot.register_next_step_handler(message, question43)

def question43(message):
    
    bot.send_message(message.chat.id, f'{func_questionlang(message.from_user.id)} 43:\n{defquestions_(message.from_user.id)[43]}', reply_markup=rkm(message.from_user.id))
    if catn(message.text, message.from_user.id) == 'error':
        bot.send_message(message.chat.id, f'{func_wronginput(message.from_user.id)}')
        bot.register_next_step_handler(message, question43)
    else:
        db.insert_answers(message.from_user.id, catn(message.text, message.from_user.id), '42')
        bot.register_next_step_handler(message, question44)

def question44(message):
    
    bot.send_message(message.chat.id, f'{func_questionlang(message.from_user.id)} 44:\n{defquestions_(message.from_user.id)[44]}', reply_markup=rkm(message.from_user.id))
    if catn(message.text, message.from_user.id) == 'error':
        bot.send_message(message.chat.id, f'{func_wronginput(message.from_user.id)}')
        bot.register_next_step_handler(message, question44)
    else:
        db.insert_answers(message.from_user.id, catn(message.text, message.from_user.id), '43')
        bot.register_next_step_handler(message, question45)

def question45(message):
    
    bot.send_message(message.chat.id, f'{func_questionlang(message.from_user.id)} 45:\n{defquestions_(message.from_user.id)[45]}', reply_markup=rkm(message.from_user.id))
    if catn(message.text, message.from_user.id) == 'error':
        bot.send_message(message.chat.id, f'{func_wronginput(message.from_user.id)}')
        bot.register_next_step_handler(message, question45)
    else:
        db.insert_answers(message.from_user.id, catn(message.text, message.from_user.id), '44')
        bot.register_next_step_handler(message, question46)

def question46(message):
    
    bot.send_message(message.chat.id, f'{func_questionlang(message.from_user.id)} 46:\n{defquestions_(message.from_user.id)[46]}', reply_markup=rkm(message.from_user.id))
    if catn(message.text, message.from_user.id) == 'error':
        bot.send_message(message.chat.id, f'{func_wronginput(message.from_user.id)}')
        bot.register_next_step_handler(message, question46)
    else:
        db.insert_answers(message.from_user.id, catn(message.text, message.from_user.id), '45')
        bot.register_next_step_handler(message, question47)

def question47(message):
    
    bot.send_message(message.chat.id, f'{func_questionlang(message.from_user.id)} 47:\n{defquestions_(message.from_user.id)[47]}', reply_markup=rkm(message.from_user.id))
    if catn(message.text, message.from_user.id) == 'error':
        bot.send_message(message.chat.id, f'{func_wronginput(message.from_user.id)}')
        bot.register_next_step_handler(message, question47)
    else:
        db.insert_answers(message.from_user.id, catn(message.text, message.from_user.id), '46')
        bot.register_next_step_handler(message, question48)

def question48(message):
    
    bot.send_message(message.chat.id, f'{func_questionlang(message.from_user.id)} 48:\n{defquestions_(message.from_user.id)[48]}', reply_markup=rkm(message.from_user.id))
    if catn(message.text, message.from_user.id) == 'error':
        bot.send_message(message.chat.id, f'{func_wronginput(message.from_user.id)}')
        bot.register_next_step_handler(message, question48)
    else:
        db.insert_answers(message.from_user.id, catn(message.text, message.from_user.id), '47')
        bot.register_next_step_handler(message, question49)

def question49(message):
    
    bot.send_message(message.chat.id, f'{func_questionlang(message.from_user.id)} 49:\n{defquestions_(message.from_user.id)[49]}', reply_markup=rkm(message.from_user.id))
    if catn(message.text, message.from_user.id) == 'error':
        bot.send_message(message.chat.id, f'{func_wronginput(message.from_user.id)}')
        bot.register_next_step_handler(message, question49)
    else:
        db.insert_answers(message.from_user.id, catn(message.text, message.from_user.id), '48')
        bot.register_next_step_handler(message, question50)

def question50(message):
    
    bot.send_message(message.chat.id, f'{func_questionlang(message.from_user.id)} 50:\n{defquestions_(message.from_user.id)[50]}', reply_markup=rkm(message.from_user.id))
    if catn(message.text, message.from_user.id) == 'error':
        bot.send_message(message.chat.id, f'{func_wronginput(message.from_user.id)}')
        bot.register_next_step_handler(message, question50)
    else:
        db.insert_answers(message.from_user.id, catn(message.text, message.from_user.id), '49')
        bot.register_next_step_handler(message, question51)

def question51(message):
    
    bot.send_message(message.chat.id, f'{func_questionlang(message.from_user.id)} 51:\n{defquestions_(message.from_user.id)[51]}', reply_markup=rkm(message.from_user.id))
    if catn(message.text, message.from_user.id) == 'error':
        bot.send_message(message.chat.id, f'{func_wronginput(message.from_user.id)}')
        bot.register_next_step_handler(message, question51)
    else:
        db.insert_answers(message.from_user.id, catn(message.text, message.from_user.id), '50')
        bot.register_next_step_handler(message, question52)

def question52(message):
    bot.send_message(message.chat.id, eval(f'lang.part5_msg_{choosenlang}'))
    
    bot.send_message(message.chat.id, f'{func_questionlang(message.from_user.id)} 52:\n{defquestions_(message.from_user.id)[52]}', reply_markup=rkm(message.from_user.id))
    if catn(message.text, message.from_user.id) == 'error':
        bot.send_message(message.chat.id, f'{func_wronginput(message.from_user.id)}')
        bot.register_next_step_handler(message, question52)
    else:
        db.insert_answers(message.from_user.id, catn(message.text, message.from_user.id), '51')
        bot.register_next_step_handler(message, question53)

def question53(message):
    
    bot.send_message(message.chat.id, f'{func_questionlang(message.from_user.id)} 53:\n{defquestions_(message.from_user.id)[53]}', reply_markup=rkm(message.from_user.id))
    if catn(message.text, message.from_user.id) == 'error':
        bot.send_message(message.chat.id, f'{func_wronginput(message.from_user.id)}')
        bot.register_next_step_handler(message, question53)
    else:
        db.insert_answers(message.from_user.id, catn(message.text, message.from_user.id), '52')
        bot.register_next_step_handler(message, question54)

def question54(message):
    
    bot.send_message(message.chat.id, f'{func_questionlang(message.from_user.id)} 54:\n{defquestions_(message.from_user.id)[54]}', reply_markup=rkm(message.from_user.id))
    if catn(message.text, message.from_user.id) == 'error':
        bot.send_message(message.chat.id, f'{func_wronginput(message.from_user.id)}')
        bot.register_next_step_handler(message, question54)
    else:
        db.insert_answers(message.from_user.id, catn(message.text, message.from_user.id), '53')
        bot.register_next_step_handler(message, question55)

def question55(message):
    
    bot.send_message(message.chat.id, f'{func_questionlang(message.from_user.id)} 55:\n{defquestions_(message.from_user.id)[55]}', reply_markup=rkm(message.from_user.id))
    if catn(message.text, message.from_user.id) == 'error':
        bot.send_message(message.chat.id, f'{func_wronginput(message.from_user.id)}')
        bot.register_next_step_handler(message, question55)
    else:
        db.insert_answers(message.from_user.id, catn(message.text, message.from_user.id), '54')
        bot.register_next_step_handler(message, question56)

def question56(message):
    
    bot.send_message(message.chat.id, f'{func_questionlang(message.from_user.id)} 56:\n{defquestions_(message.from_user.id)[56]}', reply_markup=rkm(message.from_user.id))
    if catn(message.text, message.from_user.id) == 'error':
        bot.send_message(message.chat.id, f'{func_wronginput(message.from_user.id)}')
        bot.register_next_step_handler(message, question56)
    else:
        db.insert_answers(message.from_user.id, catn(message.text, message.from_user.id), '55')
        bot.register_next_step_handler(message, question57)

def question57(message):
    bot.send_message(message.chat.id, eval(f'lang.part6_msg_{choosenlang}'))
    
    bot.send_message(message.chat.id, f'{func_questionlang(message.from_user.id)} 57:\n{defquestions_(message.from_user.id)[57]}', reply_markup=rkm(message.from_user.id))
    if catn(message.text, message.from_user.id) == 'error':
        bot.send_message(message.chat.id, f'{func_wronginput(message.from_user.id)}')
        bot.register_next_step_handler(message, question57)
    else:
        db.insert_answers(message.from_user.id, catn(message.text, message.from_user.id), '56')
        bot.register_next_step_handler(message, question58)

def question58(message):
    
    bot.send_message(message.chat.id, f'{func_questionlang(message.from_user.id)} 58:\n{defquestions_(message.from_user.id)[58]}', reply_markup=rkm(message.from_user.id))
    if catn(message.text, message.from_user.id) == 'error':
        bot.send_message(message.chat.id, f'{func_wronginput(message.from_user.id)}')
        bot.register_next_step_handler(message, question58)
    else:
        db.insert_answers(message.from_user.id, catn(message.text, message.from_user.id), '57')
        bot.register_next_step_handler(message, question59)

def question59(message):
    
    bot.send_message(message.chat.id, f'{func_questionlang(message.from_user.id)} 59:\n{defquestions_(message.from_user.id)[59]}', reply_markup=rkm(message.from_user.id))
    if catn(message.text, message.from_user.id) == 'error':
        bot.send_message(message.chat.id, f'{func_wronginput(message.from_user.id)}')
        bot.register_next_step_handler(message, question59)
    else:
        db.insert_answers(message.from_user.id, catn(message.text, message.from_user.id), '58')
        bot.register_next_step_handler(message, question60)

def question60(message):
    
    bot.send_message(message.chat.id, f'{func_questionlang(message.from_user.id)} 60:\n{defquestions_(message.from_user.id)[60]}', reply_markup=rkm(message.from_user.id))
    if catn(message.text, message.from_user.id) == 'error':
        bot.send_message(message.chat.id, f'{func_wronginput(message.from_user.id)}')
        bot.register_next_step_handler(message, question60)
    else:
        db.insert_answers(message.from_user.id, catn(message.text, message.from_user.id), '59')
        bot.register_next_step_handler(message, question61)

def question61(message):
    
    bot.send_message(message.chat.id, f'{func_questionlang(message.from_user.id)} 61:\n{defquestions_(message.from_user.id)[61]}', reply_markup=rkm(message.from_user.id))
    if catn(message.text, message.from_user.id) == 'error':
        bot.send_message(message.chat.id, f'{func_wronginput(message.from_user.id)}')
        bot.register_next_step_handler(message, question61)
    else:
        db.insert_answers(message.from_user.id, catn(message.text, message.from_user.id), '60')
        bot.register_next_step_handler(message, question62)

def question62(message):
    bot.send_message(message.chat.id, eval(f'lang.lastq_msg_{choosenlang}'))
    
    bot.send_message(message.chat.id, f'{func_questionlang(message.from_user.id)} 62:\n{defquestions_(message.from_user.id)[62]}', reply_markup=rkm(message.from_user.id))
    if catn(message.text, message.from_user.id) == 'error':
        bot.send_message(message.chat.id, f'{func_wronginput(message.from_user.id)}')
        bot.register_next_step_handler(message, question62)
    else:
        db.insert_answers(message.from_user.id, catn(message.text, message.from_user.id), '61')
        bot.register_next_step_handler(message, finish)


def finish(message):
    if catn(message.text, message.from_user.id) == 'error':
        bot.send_message(message.chat.id, f'{func_wronginput(message.from_user.id)}')
        bot.register_next_step_handler(message, finish)
    else:
        db.insert_answers(message.from_user.id, catn(message.text, message.from_user.id), '62')
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=1)
        markup.add(eval(f'lang.restart_btn_{choosenlang}'))
        wait = bot.send_message(message.chat.id, eval(f'lang.wait_msg_{choosenlang}'))
        wait
        name = message.from_user.first_name
        pcresults = pwp.results(pwp.format_answers(answers=db.format_db_answers(message.from_user.id)))
        url = f'https://www.politicalcompass.org/analysis2?{pcresults}'
        image = f'https://www.politicalcompass.org/chart?{pcresults}'
        pdf = f'https://www.politicalcompass.org/pdfcertificate?pname={name}&{pcresults}'
        linkmsg = eval(f'lang.link_msg_{choosenlang}')
        bot.delete_message(message.chat.id, wait.message_id)
        bot.send_message(message.chat.id, eval(f'lang.urpc_msg_{choosenlang}'))
        bot.send_message(message.chat.id, f'{func_elr(message.from_user.id)} \n{pcresults.split("ec=")[1].split("&")[0]}\n{func_elr(message.from_user.id)} \n{pcresults.split("soc=")[1]}')
        bot.send_photo(message.chat.id, image, caption=eval(f'lang.chart_msg_{choosenlang}')) 
        bot.send_document(message.chat.id, pdf , caption=eval(f'lang.pdf_msg_{choosenlang}'))
        bot.send_message(message.chat.id, f'{url}\n{linkmsg}')
        db.insert_result(message.from_user.id, pcresults)
        bot.send_message(message.chat.id, eval(f'lang.tnks_msg_{choosenlang}'), reply_markup=markup)

def my_resultes(message):  
    if db.check_reslt(message.from_user.id) == False:
        bot.send_message(message.chat.id, eval(f'lang.noresults_msg_{choosenlang}'))
    else:  
        name = message.from_user.first_name
        pcresults = db.get_result(message.from_user.id)
        url = f'https://www.politicalcompass.org/analysis2?{pcresults}'
        image = f'https://www.politicalcompass.org/chart?{pcresults}'
        pdf = f'https://www.politicalcompass.org/pdfcertificate?pname={name}&{pcresults}'
        linkmsg = eval(f'lang.link_msg_{choosenlang}')
        bot.send_message(message.chat.id, eval(f'lang.urpc_msg_{choosenlang}'))
        bot.send_message(message.chat.id, f'{func_elr(message.from_user.id)} \n{pcresults.split("ec=")[1].split("&")[0]}\n{func_elr(message.from_user.id)} \n{pcresults.split("soc=")[1]}')
        bot.send_photo(message.chat.id, image, caption=eval(f'lang.chart_msg_{choosenlang}')) 
        bot.send_document(message.chat.id, pdf , caption=eval(f'lang.pdf_msg_{choosenlang}'))
        bot.send_message(message.chat.id, f'{url}\n{linkmsg}')

@bot.message_handler(commands=['myresult'])
def myresult_c(message):
    my_resultes(message)

@bot.message_handler(commands=['rename'])
def rename_c(message):
    if db.check_reslt(message.from_user.id) == False:
        bot.send_message(message.chat.id, eval(f'lang.noresults_msg_{choosenlang}'))
    else:
        bot.send_message(message.chat.id, eval(f'lang.rename_msg_{choosenlang}'))
        bot.register_next_step_handler(message, rename)
def rename(message):
    name = message.text.replace(' ', '+')
    pcresults = db.get_result(message.from_user.id)
    pdf = f'https://www.politicalcompass.org/pdfcertificate?pname={name}&{pcresults}'
    bot.send_document(message.chat.id, pdf , caption=eval(f'lang.pdf_msg_{choosenlang}'))

