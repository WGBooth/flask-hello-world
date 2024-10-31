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

# creates table named Basketball
@app.route('/db_create')
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

# inserts initial players into Basketball table
@app.route('/db_insert')
def insert_players():
    conn = psycopg2.connect("postgresql://nba_players_user:PB0ky7JPS5pCvFOdThEnJXbN6xHPU3EM@dpg-cshmjce8ii6s73bhp5eg-a/nba_players")
    cur = conn.cursor()
    cur.execute('''
                INSERT INTO Basketball (First, Last, City, Name, Number)
                VALUES 
                ('Jayson', 'Tatum', 'Boston', 'Celitcs', 0),
                ('Stephen', 'Curry', 'Golden State', 'Warriors', 30),
                ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
                (Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2);
                ''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Populated"

# selects all players in Basketball table
@app.route('/db_select')
def selecting():
    conn = psycopg2.connect("postgresql://nba_players_user:PB0ky7JPS5pCvFOdThEnJXbN6xHPU3EM@dpg-cshmjce8ii6s73bhp5eg-a/nba_players")
    cur = conn.cursor()
    cur.execute('''
                SELECT * FROM Basketball;
                ''')
    records = cur.fetchall()
    conn.close()
    response_string=""
    response_string += "<table>"
    for player in records:
        response_string+="<tr>"
        for info in player:
            response_string+="<td>{}</td>".format(info)
            response_string+="<td>"
    response_string+="</table>"
    return str(records)

@app.route('/db_drop')
def dropping():
    conn = psycopg2.connect("postgresql://nba_players_user:PB0ky7JPS5pCvFOdThEnJXbN6xHPU3EM@dpg-cshmjce8ii6s73bhp5eg-a/nba_players")
    cur = conn.cursor()
    cur.execute('''
                DROP TABLE Basketball;
                ''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Dropped"