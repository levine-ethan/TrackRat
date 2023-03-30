from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    conn = sqlite3.connect('./database/trackrat.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM tracking")
    data = cur.fetchall()
    conn.close()
    return render_template('results.html', data=data)

if __name__ == '__main__':
    app.run()