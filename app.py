from flask import Flask, request, render_template, redirect, url_for
import mysql.connector
import os

app = Flask(__name__)

password = os.environ['DB_PASSWORD']

db_config = {
    'host': 'localhost',
    'user': 'max',
    'password': password,
    'database': 'flaskdb'
}

@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, email) VALUES (%s, %s)", (username, email))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('register'))
    return render_template('register.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
