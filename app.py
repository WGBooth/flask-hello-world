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

@ app.route('/db_create')
def crate_basketball():
    conn = psycopg2.connect("postgresql://nba_players_user:PB0ky7JPS5pCvFOdThEnJXbN6xHPU3EM@dpg-cshmjce8ii6s73bhp5eg-a/nba_players")
    cur = conn.cursor()
    cur.execute('''
                CREATE TABLE IF NOT EXISTS Basketball (
                First varchar(255),
                Last varchar(255),
                City varchar(255),
                Name varchar(255), 
                Number int
                );
            ''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Created"