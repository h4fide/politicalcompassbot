import sys
import telebot
from telebot import types
from config import token
import politicwebspost as pwp

bot = telebot.TeleBot(token)


def_questions = {
    1:	"If economic globalisation is inevitable, it should primarily serve humanity rather than the interests of trans-national corporations.",
    2:	"I'd always support my country, whether it was right or wrong.",
    3:	"No one chooses his or her country of birth, so it's foolish to be proud of it.",
    4:	"Our race has many superior qualities, compared with other races.",
    5:	"The enemy of my enemy is my friend.",
    6:	"Military action that defies international law is sometimes justified.",
    7:	"There is now a worrying fusion of information and entertainment.",
    8:	"People are ultimately divided more by class than by nationality.",
    9:	"Controlling inflation is more important than controlling unemployment.",
    10:	"Because corporations cannot be trusted to voluntarily protect the environment, they require regulation.",
    11:	"\"from each according to his ability, to each according to his need\" is a fundamentally good idea.",
    12:	"It's a sad reflection on our society that something as basic as drinking water is now a bottled, branded consumer product.",
    13:	"Land shouldn't be a commodity to be bought and sold.",
    14:	"It is regrettable that many personal fortunes are made by people who simply manipulate money and contribute nothing to their society.",
    15:	"Protectionism is sometimes necessary in trade.",
    16:	"The only social responsibility of a company should be to deliver a profit to its shareholders.",
    17:	"The rich are too highly taxed.",
    18:	"Those with the ability to pay should have the right to higher standards of medical care .",
    19:	"Governments should penalise businesses that mislead the public.",
    20:	"A genuine free market requires restrictions on the ability of predator multinationals to create monopolies.",
    21:	"The freer the market, the freer the people.",
    22:	"Abortion, when the woman's life is not threatened, should always be illegal.",
    23:	"All authority should be questioned.",
    24:	"An eye for an eye and a tooth for a tooth.",
    25:	"Taxpayers should not be expected to prop up any theatres or museums that cannot survive on a commercial basis.",
    26:	"Schools should not make classroom attendance compulsory.",
    27:	"All people have their rights, but it is better for all of us that different sorts of people should keep to their own kind.",
    28:	"Good parents sometimes have to spank their children.",
    29:	"It's natural for children to keep some secrets from their parents.",
    30:	"Possessing marijuana for personal use should not be a criminal offence.",
    31:	"The prime function of schooling should be to equip the future generation to find jobs.",
    32:	"People with serious inheritable disabilities should not be allowed to reproduce.",
    33:	"The most important thing for children to learn is to accept discipline.",
    34:	"There are no savage and civilised peoples; there are only different cultures.",
    35:	"Those who are able to work, and refuse the opportunity, should not expect society's support.",
    36:	"When you are troubled, it's better not to think about it, but to keep busy with more cheerful things.",
    37:	"First-generation immigrants can never be fully integrated within their new country.",
    38:	"What's good for the most successful corporations is always, ultimately, good for all of us.",
    39:	"No broadcasting institution, however independent its content, should receive public funding.",
    40:	"Our civil liberties are being excessively curbed in the name of counter-terrorism.",
    41:	"A significant advantage of a one-party state is that it avoids all the arguments that delay progress in a democratic political system.",
    42:	"Although the electronic age makes official surveillance easier, only wrongdoers need to be worried.",
    43:	"The death penalty should be an option for the most serious crimes.",
    44:	"In a civilised society, one must always have people above to be obeyed and people below to be commanded.",
    45:	"Abstract art that doesn't represent anything shouldn't be considered art at all.",
    46:	"In criminal justice, punishment should be more important than rehabilitation.",
    47:	"It is a waste of time to try to rehabilitate some criminals.",
    48:	"The businessperson and the manufacturer are more important than the writer and the artist.",
    49:	"Mothers may have careers, but their first duty is to be homemakers.",
    50:	"Multinational companies are unethically exploiting the plant genetic resources of developing countries.",
    51:	"Making peace with the establishment is an important aspect of maturity.",
    52:	"Astrology accurately explains many things.",
    53:	"You cannot be moral without being religious.",
    54:	"Charity is better than social security as a means of helping the genuinely disadvantaged.",
    55:	"Some people are naturally unlucky.",
    56:	"It is important that my child's school instills religious values.",
    57:	"Sex outside marriage is usually immoral.",
    58:	"A same sex couple in a stable, loving relationship, should not be excluded from the possibility of child adoption.",
    59:	"Pornography, depicting consenting adults, should be legal for the adult population.",
    60:	"What goes on in a private bedroom between consenting adults is no business of the state.",
    61:	"No one can feel naturally homosexual.",
    62:	"These days openness about sex has gone too far."
}

answers = []
print(' ')

def catn(replay):
    if replay == 'Strongly disagree':
        return 0
    elif replay == 'Disagree':
        return 1
    elif replay == 'Agree':
        return 2
    elif replay == 'Strongly agree':
        return 3
    else:
        return 'error'

def rkm():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=False)
    strong_disagree = "Strongly disagree"
    disagree = "Disagree"
    agree = "Agree"
    strong_agrre ="Strongly agree"
    markup.add(strong_disagree)
    markup.add(disagree)
    markup.add(agree)
    markup.add(strong_agrre)
    return markup

@bot.message_handler(commands=['help'])
def help_message(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=1)
    markup.add('Start 📝')
    bot.send_message(message.chat.id, 'Star your political compass by clicking button bellow 👇', reply_markup=markup)

@bot.message_handler(commands=['cancel'])
def cancel_message(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=1)
    markup.add('Start 📝')
    bot.send_message(message.chat.id, 'Canceled', reply_markup=markup)


@bot.message_handler(commands=['start'])
def start_message(message):
    answers.clear()
    bot.reply_to(message, """
    Ladies and gentlemen, attack helicopters, welcome to a political orientation that will force you to abandon social constructs and find your true self! A journey in the right direction begins with the right compass""")
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=False)
    markup.add('Let\'s go!')
    bot.send_message(message.chat.id, "Are you ready?", reply_markup=markup)
    bot.register_next_step_handler(message, question1)

@bot.message_handler(func=lambda message: True)
def messagess(message):
    if message.text == 'Restart 🔄' or message.text == 'Start 📝':
        start_message(message)
    else:
        bot.reply_to(message, 'Please, use command /help')

def question1(message):
    if message.text == '/cancel':
        cancel_message(message)
    else:    
        bot.send_message(message.chat.id, 'Cancel your journey by clicking /cancel')
        bot.send_message(message.chat.id, 'Part 1')
        bot.send_message(message.chat.id, f'Question 1:\n{def_questions[1]}', reply_markup=rkm())
        bot.register_next_step_handler(message, question2)
    
def question2(message):
    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    if message.text == '/cancel':
        cancel_message(message)
    else:
        bot.send_message(message.chat.id, f'Question 2:\n{def_questions[2]}', reply_markup=rkm())
        if catn(message.text) == 'error':
            bot.send_message(message.chat.id, 'Please, choose one of the options')
            bot.register_next_step_handler(message, question2)
        else:
            answers.append({1: catn(message.text)})
            bot.register_next_step_handler(message, question3)

def question3(message):
    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    if message.text == '/cancel':
        cancel_message(message)
    else:
        bot.send_message(message.chat.id, f'Question 3:\n{def_questions[3]}', reply_markup=rkm())
        if catn(message.text) == 'error':
            bot.send_message(message.chat.id, 'Please, choose one of the options')
            bot.register_next_step_handler(message, question3)
        else:
            answers.append({2: catn(message.text)})
            bot.register_next_step_handler(message, question4)

def question4(message):
    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    bot.send_message(message.chat.id, f'Question 4:\n{def_questions[4]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, 'Please, choose one of the options')
        bot.register_next_step_handler(message, question4)
    elif message.text == '/cancel':
        cancel_message(message)
    else:
        answers.append({3: catn(message.text)})
        bot.register_next_step_handler(message, question5)

def question5(message):
    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    bot.send_message(message.chat.id, f'Question 5:\n{def_questions[5]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, 'Please, choose one of the options')
        bot.register_next_step_handler(message, question5)
    else:
        answers.append({4: catn(message.text)})
        bot.register_next_step_handler(message, question6)

def question6(message):
    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    bot.send_message(message.chat.id, f'Question 6:\n{def_questions[6]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, 'Please, choose one of the options')
        bot.register_next_step_handler(message, question6)
    else:
        answers.append({5: catn(message.text)})
        bot.register_next_step_handler(message, question7)

def question7(message):
    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    bot.send_message(message.chat.id, f'Question 7:\n{def_questions[7]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, 'Please, choose one of the options')
        bot.register_next_step_handler(message, question7)
    else:
        answers.append({6: catn(message.text)})
        bot.register_next_step_handler(message, question8)

def question8(message):
    bot.send_message(message.chat.id, 'Part 2')
    bot.send_message(message.chat.id, f'Question 8:\n{def_questions[8]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, 'Please, choose one of the options')
        bot.register_next_step_handler(message, question8)
    else:
        answers.append({7: catn(message.text)})
        bot.register_next_step_handler(message, question9)

def question9(message):

    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    bot.send_message(message.chat.id, f'Question 9:\n{def_questions[9]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, 'Please, choose one of the options')
        bot.register_next_step_handler(message, question9)
    else:
        answers.append({8: catn(message.text)})
        bot.register_next_step_handler(message, question10)

def question10(message):
    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    bot.send_message(message.chat.id, f'Question 10:\n{def_questions[10]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, 'Please, choose one of the options')
        bot.register_next_step_handler(message, question10)
    else:
        answers.append({9: catn(message.text)})
        bot.register_next_step_handler(message, question11)

def question11(message):
    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    bot.send_message(message.chat.id, f'Question 11:\n{def_questions[11]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, 'Please, choose one of the options')
        bot.register_next_step_handler(message, question11)
    else:
        answers.append({10: catn(message.text)})
        bot.register_next_step_handler(message, question12)

def question12(message):
    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    bot.send_message(message.chat.id, f'Question 12:\n{def_questions[12]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, 'Please, choose one of the options')
        bot.register_next_step_handler(message, question12)
    else:
        answers.append({11: catn(message.text)})
        bot.register_next_step_handler(message, question13)

def question13(message):
    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    bot.send_message(message.chat.id, f'Question 13:\n{def_questions[13]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, 'Please, choose one of the options')
        bot.register_next_step_handler(message, question13)
    else:
        answers.append({12: catn(message.text)})
        bot.register_next_step_handler(message, question14)

def question14(message):
    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    bot.send_message(message.chat.id, f'Question 14:\n{def_questions[14]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, 'Please, choose one of the options')
        bot.register_next_step_handler(message, question14)
    else:
        answers.append({13: catn(message.text)})
        bot.register_next_step_handler(message, question15)

def question15(message):
    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    bot.send_message(message.chat.id, f'Question 15:\n{def_questions[15]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, 'Please, choose one of the options')
        bot.register_next_step_handler(message, question15)
    else:
        answers.append({14: catn(message.text)})
        bot.register_next_step_handler(message, question16)

def question16(message):
    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    bot.send_message(message.chat.id, f'Question 16:\n{def_questions[16]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, 'Please, choose one of the options')
        bot.register_next_step_handler(message, question16)
    else:
        answers.append({15: catn(message.text)})
        bot.register_next_step_handler(message, question17)

def question17(message):
    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    bot.send_message(message.chat.id, f'Question 17:\n{def_questions[17]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, 'Please, choose one of the options')
        bot.register_next_step_handler(message, question17)
    else:
        answers.append({16: catn(message.text)})
        bot.register_next_step_handler(message, question18)

def question18(message):
    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    bot.send_message(message.chat.id, f'Question 18:\n{def_questions[18]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, 'Please, choose one of the options')
        bot.register_next_step_handler(message, question18)
    else:
        answers.append({17: catn(message.text)})
        bot.register_next_step_handler(message, question19)

def question19(message):
    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    bot.send_message(message.chat.id, f'Question 19:\n{def_questions[19]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, 'Please, choose one of the options')
        bot.register_next_step_handler(message, question19)
    else:
        answers.append({18: catn(message.text)})
        bot.register_next_step_handler(message, question20)

def question20(message):
    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    bot.send_message(message.chat.id, f'Question 20:\n{def_questions[20]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, 'Please, choose one of the options')
        bot.register_next_step_handler(message, question20)
    else:
        answers.append({19: catn(message.text)})
        bot.register_next_step_handler(message, question21)

def question21(message):
    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    bot.send_message(message.chat.id, f'Question 21:\n{def_questions[21]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, 'Please, choose one of the options')
        bot.register_next_step_handler(message, question21)
    else:
        answers.append({20: catn(message.text)})
        bot.register_next_step_handler(message, question22)

def question22(message):
    bot.send_message(message.chat.id, 'Part 3')
    bot.send_message(message.chat.id, f'Question 22:\n{def_questions[22]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, 'Please, choose one of the options')
        bot.register_next_step_handler(message, question22)
    else:
        answers.append({21: catn(message.text)})
        bot.register_next_step_handler(message, question23)

def question23(message):
    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    bot.send_message(message.chat.id, f'Question 23:\n{def_questions[23]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, 'Please, choose one of the options')
        bot.register_next_step_handler(message, question23)
    else:
        answers.append({22: catn(message.text)})
        bot.register_next_step_handler(message, question24)

def question24(message):
    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    bot.send_message(message.chat.id, f'Question 24:\n{def_questions[24]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, 'Please, choose one of the options')
        bot.register_next_step_handler(message, question24)
    else:
        answers.append({23: catn(message.text)})
        bot.register_next_step_handler(message, question25)

def question25(message):
    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    bot.send_message(message.chat.id, f'Question 25:\n{def_questions[25]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, 'Please, choose one of the options')
        bot.register_next_step_handler(message, question25)
    else:
        answers.append({24: catn(message.text)})
        bot.register_next_step_handler(message, question26)

def question26(message):
    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    bot.send_message(message.chat.id, f'Question 26:\n{def_questions[26]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, 'Please, choose one of the options')
        bot.register_next_step_handler(message, question26)
    else:
        answers.append({25: catn(message.text)})
        bot.register_next_step_handler(message, question27)

def question27(message):
    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    bot.send_message(message.chat.id, f'Question 27:\n{def_questions[27]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, 'Please, choose one of the options')
        bot.register_next_step_handler(message, question27)
    else:
        answers.append({26: catn(message.text)})
        bot.register_next_step_handler(message, question28)

def question28(message):
    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    bot.send_message(message.chat.id, f'Question 28:\n{def_questions[28]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, 'Please, choose one of the options')
        bot.register_next_step_handler(message, question28)
    else:
        answers.append({27: catn(message.text)})
        bot.register_next_step_handler(message, question29)

def question29(message):
    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    bot.send_message(message.chat.id, f'Question 29:\n{def_questions[29]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, 'Please, choose one of the options')
        bot.register_next_step_handler(message, question29)
    else:
        answers.append({28: catn(message.text)})
        bot.register_next_step_handler(message, question30)

def question30(message):
    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    bot.send_message(message.chat.id, f'Question 30:\n{def_questions[30]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, 'Please, choose one of the options')
        bot.register_next_step_handler(message, question30)
    else:
        answers.append({29: catn(message.text)})
        bot.register_next_step_handler(message, question31)

def question31(message):
    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    bot.send_message(message.chat.id, f'Question 31:\n{def_questions[31]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, 'Please, choose one of the options')
        bot.register_next_step_handler(message, question31)
    else:
        answers.append({30: catn(message.text)})
        bot.register_next_step_handler(message, question32)

def question32(message):
    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    bot.send_message(message.chat.id, f'Question 32:\n{def_questions[32]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, 'Please, choose one of the options')
        bot.register_next_step_handler(message, question32)
    else:
        answers.append({31: catn(message.text)})
        bot.register_next_step_handler(message, question33)

def question33(message):
    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    bot.send_message(message.chat.id, f'Question 33:\n{def_questions[33]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, 'Please, choose one of the options')
        bot.register_next_step_handler(message, question33)
    else:
        answers.append({32: catn(message.text)})
        bot.register_next_step_handler(message, question34)

def question34(message):
    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    bot.send_message(message.chat.id, f'Question 34:\n{def_questions[34]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, 'Please, choose one of the options')
        bot.register_next_step_handler(message, question34)
    else:
        answers.append({33: catn(message.text)})
        bot.register_next_step_handler(message, question35)

def question35(message):
    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    bot.send_message(message.chat.id, f'Question 35:\n{def_questions[35]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, 'Please, choose one of the options')
        bot.register_next_step_handler(message, question35)
    else:
        answers.append({34: catn(message.text)})
        bot.register_next_step_handler(message, question36)

def question36(message):
    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    bot.send_message(message.chat.id, f'Question 36:\n{def_questions[36]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, 'Please, choose one of the options')
        bot.register_next_step_handler(message, question36)
    else:
        answers.append({35: catn(message.text)})
        bot.register_next_step_handler(message, question37)

def question37(message):
    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    bot.send_message(message.chat.id, f'Question 37:\n{def_questions[37]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, 'Please, choose one of the options')
        bot.register_next_step_handler(message, question37)
    else:
        answers.append({36: catn(message.text)})
        bot.register_next_step_handler(message, question38)

def question38(message):
    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    bot.send_message(message.chat.id, f'Question 38:\n{def_questions[38]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, 'Please, choose one of the options')
        bot.register_next_step_handler(message, question38)
    else:
        answers.append({37: catn(message.text)})
        bot.register_next_step_handler(message, question39)

def question39(message):
    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    bot.send_message(message.chat.id, f'Question 39:\n{def_questions[39]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, 'Please, choose one of the options')
        bot.register_next_step_handler(message, question39)
    else:
        answers.append({38: catn(message.text)})
        bot.register_next_step_handler(message, question40)

def question40(message):
    bot.send_message(message.chat.id, 'Part 4')
    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    bot.send_message(message.chat.id, f'Question 40:\n{def_questions[40]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, 'Please, choose one of the options')
        bot.register_next_step_handler(message, question40)
    else:
        answers.append({39: catn(message.text)})
        bot.register_next_step_handler(message, question41)

def question41(message):
    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    bot.send_message(message.chat.id, f'Question 41:\n{def_questions[41]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, 'Please, choose one of the options')
        bot.register_next_step_handler(message, question41)
    else:
        answers.append({40: catn(message.text)})
        bot.register_next_step_handler(message, question42)
    
def question42(message):
    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    bot.send_message(message.chat.id, f'Question 42:\n{def_questions[42]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, 'Please, choose one of the options')
        bot.register_next_step_handler(message, question42)
    else:
        answers.append({41: catn(message.text)})
        bot.register_next_step_handler(message, question43)

def question43(message):
    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    bot.send_message(message.chat.id, f'Question 43:\n{def_questions[43]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, 'Please, choose one of the options')
        bot.register_next_step_handler(message, question43)
    else:
        answers.append({42: catn(message.text)})
        bot.register_next_step_handler(message, question44)

def question44(message):
    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    bot.send_message(message.chat.id, f'Question 44:\n{def_questions[44]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, 'Please, choose one of the options')
        bot.register_next_step_handler(message, question44)
    else:
        answers.append({43: catn(message.text)})
        bot.register_next_step_handler(message, question45)

def question45(message):
    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    bot.send_message(message.chat.id, f'Question 45:\n{def_questions[45]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, 'Please, choose one of the options')
        bot.register_next_step_handler(message, question45)
    else:
        answers.append({44: catn(message.text)})
        bot.register_next_step_handler(message, question46)

def question46(message):
    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    bot.send_message(message.chat.id, f'Question 46:\n{def_questions[46]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, 'Please, choose one of the options')
        bot.register_next_step_handler(message, question46)
    else:
        answers.append({45: catn(message.text)})
        bot.register_next_step_handler(message, question47)

def question47(message):
    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    bot.send_message(message.chat.id, f'Question 47:\n{def_questions[47]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, 'Please, choose one of the options')
        bot.register_next_step_handler(message, question47)
    else:
        answers.append({46: catn(message.text)})
        bot.register_next_step_handler(message, question48)

def question48(message):
    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    bot.send_message(message.chat.id, f'Question 48:\n{def_questions[48]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, 'Please, choose one of the options')
        bot.register_next_step_handler(message, question48)
    else:
        answers.append({47: catn(message.text)})
        bot.register_next_step_handler(message, question49)

def question49(message):
    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    bot.send_message(message.chat.id, f'Question 49:\n{def_questions[49]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, 'Please, choose one of the options')
        bot.register_next_step_handler(message, question49)
    else:
        answers.append({48: catn(message.text)})
        bot.register_next_step_handler(message, question50)

def question50(message):
    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    bot.send_message(message.chat.id, f'Question 50:\n{def_questions[50]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, 'Please, choose one of the options')
        bot.register_next_step_handler(message, question50)
    else:
        answers.append({49: catn(message.text)})
        bot.register_next_step_handler(message, question51)

def question51(message):
    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    bot.send_message(message.chat.id, f'Question 51:\n{def_questions[51]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, 'Please, choose one of the options')
        bot.register_next_step_handler(message, question51)
    else:
        answers.append({50: catn(message.text)})
        bot.register_next_step_handler(message, question52)

def question52(message):
    bot.send_message(message.chat.id, 'Part 5')
    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    bot.send_message(message.chat.id, f'Question 52:\n{def_questions[52]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, 'Please, choose one of the options')
        bot.register_next_step_handler(message, question52)
    else:
        answers.append({51: catn(message.text)})
        bot.register_next_step_handler(message, question53)

def question53(message):
    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    bot.send_message(message.chat.id, f'Question 53:\n{def_questions[53]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, 'Please, choose one of the options')
        bot.register_next_step_handler(message, question53)
    else:
        answers.append({52: catn(message.text)})
        bot.register_next_step_handler(message, question54)

def question54(message):
    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    bot.send_message(message.chat.id, f'Question 54:\n{def_questions[54]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, 'Please, choose one of the options')
        bot.register_next_step_handler(message, question54)
    else:
        answers.append({53: catn(message.text)})
        bot.register_next_step_handler(message, question55)

def question55(message):
    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    bot.send_message(message.chat.id, f'Question 55:\n{def_questions[55]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, 'Please, choose one of the options')
        bot.register_next_step_handler(message, question55)
    else:
        answers.append({54: catn(message.text)})
        bot.register_next_step_handler(message, question56)

def question56(message):
    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    bot.send_message(message.chat.id, f'Question 56:\n{def_questions[56]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, 'Please, choose one of the options')
        bot.register_next_step_handler(message, question56)
    else:
        answers.append({55: catn(message.text)})
        bot.register_next_step_handler(message, question57)

def question57(message):
    bot.send_message(message.chat.id, 'Part 6: The last part')
    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    bot.send_message(message.chat.id, f'Question 57:\n{def_questions[57]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, 'Please, choose one of the options')
        bot.register_next_step_handler(message, question57)
    else:
        answers.append({56: catn(message.text)})
        bot.register_next_step_handler(message, question58)

def question58(message):
    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    bot.send_message(message.chat.id, f'Question 58:\n{def_questions[58]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, 'Please, choose one of the options')
        bot.register_next_step_handler(message, question58)
    else:
        answers.append({57: catn(message.text)})
        bot.register_next_step_handler(message, question59)

def question59(message):
    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    bot.send_message(message.chat.id, f'Question 59:\n{def_questions[59]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, 'Please, choose one of the options')
        bot.register_next_step_handler(message, question59)
    else:
        answers.append({58: catn(message.text)})
        bot.register_next_step_handler(message, question60)

def question60(message):
    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    bot.send_message(message.chat.id, f'Question 60:\n{def_questions[60]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, 'Please, choose one of the options')
        bot.register_next_step_handler(message, question60)
    else:
        answers.append({59: catn(message.text)})
        bot.register_next_step_handler(message, question61)

def question61(message):
    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    bot.send_message(message.chat.id, f'Question 61:\n{def_questions[61]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, 'Please, choose one of the options')
        bot.register_next_step_handler(message, question61)
    else:
        answers.append({60: catn(message.text)})
        bot.register_next_step_handler(message, question62)

def question62(message):
    bot.send_message(message.chat.id, 'Last Question')
    #bot.send_message(message.chat.id, 'Your answer: ' + message.text)
    bot.send_message(message.chat.id, f'Question 62:\n{def_questions[62]}', reply_markup=rkm())
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, 'Please, choose one of the options')
        bot.register_next_step_handler(message, question62)
    else:
        answers.append({61: catn(message.text)})
        bot.register_next_step_handler(message, finish)


def finish(message):
    # bot.send_message(message.chat.id, f"Your answer: {message.text}")
    if catn(message.text) == 'error':
        bot.send_message(message.chat.id, 'Please, choose one of the options')
        bot.register_next_step_handler(message, finish)
    else:
        answers.append({62: catn(message.text)})
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=1)
        markup.add('Restart 🔄')
        wait = bot.send_message(message.chat.id, "Wait Please ⏳")
        wait
        name = message.from_user.first_name
        pcresults = pwp.results(pwp.format_answers(answers=answers))
        url = f'https://www.politicalcompass.org/analysis2?{pcresults}'
        image = f'https://www.politicalcompass.org/chart?{pcresults}'
        pdf = f'https://www.politicalcompass.org/pdfcertificate?pname={name}&{pcresults}'
        bot.delete_message(message.chat.id, wait.message_id)
        bot.send_message(message.chat.id, 'Your Political Compass')
        bot.send_message(message.chat.id, f'Economic Left/Right: {pcresults.split("ec=")[1].split("&")[0]}\nSocial Libertarian/Authoritarian: {pcresults.split("soc=")[1]}')
        bot.send_photo(message.chat.id, image, caption='Take a look at your chart') 
        bot.send_document(message.chat.id, pdf , caption='Here is your certificate')
        bot.send_message(message.chat.id, 'Here is your link')
        bot.send_message(message.chat.id, url)
        bot.send_message(message.chat.id, 'Thank you for using this bot! \nIf you want to restart, press the button below', reply_markup=markup)
