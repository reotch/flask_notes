import os
import sqlite3
import markdown

from flask import Flask, render_template, request, flash, redirect, url_for
from dotenv import load_dotenv

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

app = Flask(__name__)
load_dotenv()

@app.route('/')
def index():
    conn = get_db_connection()
    db_notes = conn.execute('SELECT id, created, content FROM notes;').fetchall()
    conn.close()

    notes = []
    for note in db_notes:
        note = dict(note)
        note['content'] = markdown.markdown(note['content'])
        notes.append(note)

    notes.reverse()

    return render_template('index.html', notes=notes)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/create/', methods=('GET', 'POST'))
def create():
    conn = get_db_connection()

    if request.method == 'POST':
        content = request.form['content']
        if not content:
            flash('Content is required')
            return redirect(url_for('index'))
        conn.execute('INSERT INTO notes (content) VALUES (?)', (content,))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))

    return render_template('create.html')

if __name__ == '__main__':
    app.run()