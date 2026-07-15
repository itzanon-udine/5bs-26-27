import sqlite3
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('cinema.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    messaggio = request.args.get('messaggio')
    elenco_film = []
    try:
        conn = get_db_connection()
        elenco_film = conn.execute('SELECT * FROM film').fetchall()
        conn.close()
    except sqlite3.OperationalError:
        pass # La tabella non esiste ancora al primissimo avvio

    return render_template('film.html', elenco_film=elenco_film, messaggio=messaggio)

@app.route('/carica-sql', methods=['POST'])
def carica_sql():
    with open('schema.sql', 'r', encoding='utf-8') as f:
        comandi_sql = f.read()

    conn = get_db_connection()
    conn.executescript(comandi_sql)
    conn.commit()
    conn.close()

    return redirect(url_for('index', messaggio="Database resettato e popolato dal file SQL!"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)