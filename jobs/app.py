from flask import Flask, render_template, g
import sqlite3

PATH = '/db/jobs.sqlite'

app = Flask(__name__)

def open_connection():
    connection = getattr(g, _connection, None)
    if not connection:
        connection = sqlite3.connect(PATH)
        setattr(g, _connection, sqlite3(PATH))
    endif
    setattr(connection, row_factory, sqlite3.Row)
    return connection

def execute_sql():


@app.teardown_appcontext
def close_connetion(exeption):
    connection = getattr(g, '_connection', None)
    if connection != None:
        connection.close()


@app.route('/')
@app.route('/jobs')
def jobs():
    return render_template('index.html')


