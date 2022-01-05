import sqlite3 as db
from datetime import datetime

con = db.connect('spent.db')
cur = con.cursor()

def init():
    cur.execute('''CREATE TABLE IF NOT EXISTS expenses (
        amount REAL,
        category TEXT COLLATE NOCASE,
        message TEXT,
        date TEXT
        )''')
    con.commit()
    con.close()
    
def add(amount, category, message = ''):
    date = str(datetime.now().strftime('%Y - %m - %d | %H:%M'))
    cur.execute('INSERT INTO expenses VALUES (:amount, :category, :message, :date)', {'amount': amount, 'category': category, 'message': message, 'date': date})
    con.commit()
    con.close()
    
def show(category=None):
    if category:
        cur.execute('SELECT * FROM expenses WHERE category = (:category)', {'category' : category})
        results = cur.fetchall()
        cur.execute('SELECT SUM(amount) FROM expenses WHERE category = (:category)', {'category' : category})
        total_amount = cur.fetchone()[0]
        
    else:
        cur.execute('''SELECT * FROM expenses''')
        results = cur.fetchall()
        cur.execute('''SELECT SUM(amount) FROM expenses''')
        total_amount = cur.fetchone()[0]
        
    return total_amount,results
    con.close()
    
def remove(category):
    cur.execute('DELETE FROM expenses WHERE category = (:category)', {'category' : category})
    con.commit()
    con.close()

# init()
# add(100, 'coffee', 'message')
# print(show('coffee'))