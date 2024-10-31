import psycopg2
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from William Booth in 3308!'

@app.route('/db_test')
def db_test():
    conn = psycopg2.connect("postgresql://nba_players_user:PB0ky7JPS5pCvFOdThEnJXbN6xHPU3EM@dpg-cshmjce8ii6s73bhp5eg-a/nba_players")
    conn.close()
    return "Database Connection Successful"