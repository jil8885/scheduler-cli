from flask import Flask, jsonify
from pathlib import Path
import sqlite3
home_dir = str(Path.home())
app = Flask(__name__)

def scheduler_server():
    conn = sqlite3.connect(home_dir + '/server.db')
    cur = conn.cursor()
    create_db = 'create table if not exists server(user text not null, category text not null, month integer not null, day integer not null, what text not null, done integer)'
    cur.execute(create_db)
    conn.close()
    app.run(host='0.0.0.0', port=8865)


@app.route('/pull/<user_id>', methods=['GET'])
def pull_user(user_id):
    conn = sqlite3.connect(home_dir + '/server.db')
    cur = conn.cursor()
    select_data = 'select * from server where user_id=?'
    cur.execute(select_data, (user_id,))
    result = cur.fetchall()
    data = {'result': result}
    return jsonify(data)