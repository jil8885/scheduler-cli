import sqlite3, os
from pathlib import Path
from .valid_date import valid_date
from .make_string import make_string
from slacker import Slacker
import websocket
home_dir = str(Path.home())
def handler(command, user):
    conn = sqlite3.connect(home_dir + '/server.db')
    cur = conn.cursor()
    create_db = 'create table if not exists server(user text not null, year integer not null, category text not null, month integer not null, day integer not null, what text not null, done integer)'
    cur.execute(create_db)
    conn.close()
    command_list = command.split(' ')
    if command_list[0] == '!scheduler':
        string = input_command(command_list[1:], user)
        return string
    



def input_command(command, user):
    if command[0] == 'add':
        if '/' in command[1] and len(command[1].split('/')) == 3:
            year, month, day = command[1].split('/')
            if int(year) > 9999:
                print("Please input year under 10000")
                return 1
            if not valid_date(int(year), int(month), int(day)):
                print("Date is not valid")
                return 1
            # in 키워드를 통해 어느 category에 넣을지 정할 수 있다.
            if 'in' in command:
                category_split = command.index('in')
                category_list = command[category_split + 1:]
                content_list = command[2:category_split]
            # in 키워드가 없으면 no category 처리한다.
            else:
                category = 'No category'
                content_list = command[2:]
            # content, category를 띄어쓰기로 묶기
            content = ''
            for x in content_list:
                content += x + ' '
            if len(content) > 22:
                print("plz enter content less than 20 letters")
                return 1
            category = ''
            if 'in' in command:
                for x in category_list:
                    category += x + ' '
            else:
                category = "No category"
            category = category.strip()
            content = content.strip()
            add_cal(category, int(year), int(month), int(day), content, 0, user)
            string = 'add ok'
    elif command[0] == 'show':
        if len(command) > 2 and command[1] == 'in':
            cat = ''
            for x in command[2:]:
                cat += x + ' '
            result = return_cal_cat(user, cat.strip())
            string = make_string(result)
        elif len(command) == 2 and command[1] == 'all':
            result = return_cal(user)
            string = make_string(result)
    elif command[0] == 'delete':
        if len(command) > 2 and command[1] == 'in':
            cat = ''
            for x in command[2:]:
                cat += x + ' '
            delete_cal_cat(user, cat.strip())
            result = return_cal(user)
            string = make_string(result)
        elif len(command) == 2 and command[1] == 'all':
            result = return_cal(user)
            string = make_string(result)
        elif len(command) > 1:
            content = ''
            for x in command[1:]:
                content += x + ' '
            delete_cal(user, content.strip())
            result = return_cal(user)
            string = make_string(result)
    else:
        string = '!scheduler add {due} {content} in {category}\n!scheduler show all\n!scheduler show in {category}'
    return string

 
def return_cal_cat(user, category):
    conn = sqlite3.connect(home_dir + '/server.db')
    cur = conn.cursor()
    select_data = 'select * from server where user=? and category=?'
    cur.execute(select_data, (user,category,))
    result = cur.fetchall()
    conn.close()
    return result



def return_cal(user):
    conn = sqlite3.connect(home_dir + '/server.db')
    cur = conn.cursor()
    select_data = 'select * from server where user=?'
    cur.execute(select_data, (user,))
    result = cur.fetchall()
    conn.close()
    return result

def delete_cal_cat(user, category):
    conn = sqlite3.connect(home_dir + '/server.db')
    cur = conn.cursor()
    select_data = 'delete from server where user=? and category=?'
    cur.execute(select_data, (user,category,))
    conn.commit()
    conn.close()

def delete_cal(user, content):
    conn = sqlite3.connect(home_dir + '/server.db')
    cur = conn.cursor()
    select_data = 'delete from server where user=? and content = ?'
    cur.execute(select_data, (user,))
    conn.close()

def delete_cal_all(user):
    conn = sqlite3.connect(home_dir + '/server.db')
    cur = conn.cursor()
    select_data = 'delete from server where user=?'
    cur.execute(select_data, (user,))
    conn.close()

def add_cal(category, year, month, day, content, finished, user):
    conn = sqlite3.connect(home_dir + '/server.db')
    cur = conn.cursor()
    insert_db = 'insert into server (year, user, category, month, day, what, done) values (?,?,?,?,?,?,?)'
    cur.execute(insert_db,(year, user, category, month, day, content, finished,))
    conn.commit()
    conn.close()
