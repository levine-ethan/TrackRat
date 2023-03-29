import sqlite3
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Connect to the database
    conn = sqlite3.connect('.databases/trackrat.db')
    c = conn.cursor()

    # Execute the query
    c.execute('SELECT * FROM tracking')

    # Fetch the results
    data = c.fetchall()

    # Close the connection
    conn.close()

    # Render the results in an HTML template
    return render_template('../pages/package.html', data=data)

if __name__ == '__main__':
    app.run()