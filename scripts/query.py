from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    conn = sqlite3.connect('./databases/trackrat.db')
    c = conn.cursor()
    c.execute("SELECT * FROM tracking")
    data = c.fetchall()
    if data:
        results = []
        for row in data:
            origin, destination, current_location = row[1], row[2], row[3]
            results.append({'origin': origin, 'destination': destination, 'current_location': current_location})
        return render_template('tracking.html', results=results)
    else:
        return "No data found in tracking table"

if __name__ == '__main__':
    app.run()