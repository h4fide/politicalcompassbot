import sqlite3

path = r"db.db"

conn = sqlite3.connect(path, check_same_thread=False)
c = conn.cursor()

def createtable():
    c.execute("""CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, userid INTEGER, username TEXT,
            name TEXT, language TEXT, resultes TEXT,
            q1 INT DEFAULT 0, q2 INT DEFAULT 0, q3 INT DEFAULT 0, q4 INT DEFAULT 0, q5 INT DEFAULT 0,
            q6 INT DEFAULT 0, q7 INT DEFAULT 0, q8 INT DEFAULT 0, q9 INT DEFAULT 0, q10 INT DEFAULT 0,
            q11 INT DEFAULT 0, q12 INT DEFAULT 0, q13 INT DEFAULT 0, q14 INT DEFAULT 0, q15 INT DEFAULT 0,
            q16 INT DEFAULT 0, q17 INT DEFAULT 0, q18 INT DEFAULT 0, q19 INT DEFAULT 0, q20 INT DEFAULT 0,
            q21 INT DEFAULT 0, q22 INT DEFAULT 0, q23 INT DEFAULT 0, q24 INT DEFAULT 0, q25 INT DEFAULT 0,
            q26 INT DEFAULT 0, q27 INT DEFAULT 0, q28 INT DEFAULT 0, q29 INT DEFAULT 0, q30 INT DEFAULT 0,
            q31 INT DEFAULT 0, q32 INT DEFAULT 0, q33 INT DEFAULT 0, q34 INT DEFAULT 0, q35 INT DEFAULT 0,
            q36 INT DEFAULT 0, q37 INT DEFAULT 0, q38 INT DEFAULT 0, q39 INT DEFAULT 0, q40 INT DEFAULT 0,
            q41 INT DEFAULT 0, q42 INT DEFAULT 0, q43 INT DEFAULT 0, q44 INT DEFAULT 0, q45 INT DEFAULT 0,
            q46 INT DEFAULT 0, q47 INT DEFAULT 0, q48 INT DEFAULT 0, q49 INT DEFAULT 0, q50 INT DEFAULT 0,
            q51 INT DEFAULT 0, q52 INT DEFAULT 0, q53 INT DEFAULT 0, q54 INT DEFAULT 0, q55 INT DEFAULT 0,
            q56 INT DEFAULT 0, q57 INT DEFAULT 0, q58 INT DEFAULT 0, q59 INT DEFAULT 0, q60 INT DEFAULT 0,
            q61 INT DEFAULT 0, q62 INT DEFAULT 0)""")
    conn.commit()

def add_user(userid, username, name, language, answers_):
    c.execute("INSERT INTO users (userid, username, name, language, resultes) VALUES (?, ?, ?, ?, ?)",
                (userid, username, name, language, answers_))
    conn.commit()

def usercheck(userid):
    c.execute('SELECT * FROM users WHERE userid = ?', (userid,))
    if c.fetchone() is None:
        return False
    else:
        return True

def changeuserlang(userid, language):
    c.execute("UPDATE users SET language = ? WHERE userid = ?", (language, userid))
    conn.commit()
    
def userlanguage(userid):
    c.execute('SELECT language FROM users WHERE userid = ?', (userid,))
    return c.fetchone()[0]

def insert_result(result, userid):
    c.execute("UPDATE users SET resultes = ? WHERE userid = ?", (result, userid))
    conn.commit()
    
def insert_answers(userid, answer: int, question: str):
    c.execute(f"UPDATE users SET q{question} = {answer} WHERE userid = {userid}")
    conn.commit()

def get_answers(userid):
    c.execute('SELECT * FROM users WHERE userid = ?', (userid,))
    return c.fetchone()[6:]

def get_result(userid):
    c.execute('SELECT resultes FROM users WHERE userid = ?', (userid,))
    return c.fetchone()[0]

def format_db_answers(userid):
    answers = []
    for i in range(1, 63):
        answers.append({i:get_answers(userid)[i-1]})
    return answers

def check_reslt(userid):
    c.execute('SELECT resultes FROM users WHERE userid = ?', (userid,))
    if c.fetchone()[0] == 'null':
        return False
    else:
        return True
