from flask import Flask
import sqlite3
app = Flask(__name__)
def inti():
    conn = sqlite3.connect('mydb.db')
    with app.open_resource('db.sql', mode='r') as f:
        conn.cursor().executescript(f.read())
        print(f.read())
        conn.cursor().execute(f.read())
        conn.commit()




    conn.close()

if __name__ == "__main__":
    inti()