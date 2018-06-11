import sqlite3
from pathlib import Path
home_dir = str(Path.home())
def handler(command, user):
    conn = sqlite3.connect(home_dir + '/server.db')
    cur = conn.cursor()
    create_db = 'create table if not exists server(user text not null, year integer not null, category text not null, month integer not null, day integer not null, what text not null, done integer)'
    cur.execute(create_db)
    conn.close()
    command_list = command.split(' ')
    print(command_list)


def return_cal(command, user):
    conn = sqlite3.connect(home_dir + '/server.db')
    cur = conn.cursor()
    select_data = 'select * from server where user=?'
    cur.execute(select_data, (user,))
    result = cur.fetchall()
    return result

def add_cal(command, user):
    conn = sqlite3.connect(home_dir + '/server.db')
    cur = conn.cursor()
    delete_db = 'delete from server where user=? and what=?'
    insert_db = 'insert into server (year, user, category, month, day, what, done) values (?,?,?,?,?,?,?)'