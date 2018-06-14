from flask import Flask, jsonify, request
from pathlib import Path
import sqlite3, sys
from . import __version__
home_dir = str(Path.home())
app = Flask(__name__)
# 일정 추가시 유효한 날짜인지 구별하는 함수
def valid_date(year, month, day):
	if not(0 < month< 13):
		return False
	mth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
		mth[1] = 29
	return 0 < day and day<mth[month-1] + 1


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

def scheduler_server():
    if len(sys.argv) == 2 and sys.argv[1] in ['version', 'ver', '--v']:
        print('scheduler-server version:' + __version__)
    elif len(sys.argv) == 1:
        conn = sqlite3.connect(home_dir + '/server.db')
        cur = conn.cursor()
        create_db = 'create table if not exists server(user text not null, year integer not null, category text not null, month integer not null, day integer not null, what text not null, done integer)'
        cur.execute(create_db)
        conn.close()
        app.run(host='0.0.0.0', port=8865)
    else:
        command = sys.argv[1:]
        if command[0] == 'add':
            if '/' in command[1] and len(command[1].split('/')) == 3:
                if command[-2] == 'at':
                    user = command[-1]
                else:
                    user = 'all' 
                year, month, day = command[1].split('/')
                command = command[:-2]
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
        elif command[0] == 'delete':
            if command[-2] == 'at':
                user = command[-1]
            else:
                user = 'all' 
            if len(command) == 3 and command[-2] == 'at':
                delete_cal_all(user)



@app.route('/pull/<user_id>')
def pull_user(user_id):
    conn = sqlite3.connect(home_dir + '/server.db')
    cur = conn.cursor()
    select_data = 'select * from server where user=?'
    cur.execute(select_data, (user_id,))
    result = cur.fetchall()
    cur.execute(select_data, ('all',))
    result += cur.fetchall()    
    data = {'account': user_id, 'result': result}
    print("calender from", user_id, "is pulled from server")
    return jsonify(data)


@app.route('/push/<user_id>', methods=['POST'])
def push_userr(user_id):
    conn = sqlite3.connect(home_dir + '/server.db')
    cur = conn.cursor()
    delete_db = 'delete from server where user=? and what=?'
    insert_db = 'insert into server (user, year, category, month, day, what, done) values (?,?,?,?,?,?,?)'
    received_json = request.get_json()
    content = received_json['result']
    for x in content:
        cal = [user_id] + x
        print(cal)
        cur.execute(delete_db, (cal[1], cal[4],))
        cur.execute(insert_db, cal)
    conn.commit()
    conn.close()
    print("calender from", user_id, "is pushed to server")
    return "You pushed your data", 200
