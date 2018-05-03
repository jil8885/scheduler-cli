def sqlite_test():
	import sqlite3
	 
	# SQLite DB파일을 생성하거나 연결합니다.
	conn = sqlite3.connect("lab.db")
	 
	# Connection 으로부터 Cursor를 생성합니다.
	cur = conn.cursor()
	 
	table_create_sql = """create table if not exists todo (
				id integer primary key autoincrement,
				what text not null,
				due text not null);"""

	# 테이블을 만듭니다.
	cur.execute(table_create_sql)
	# print("created")
	wh = input("What? ")
	du = input("Due? ")
	sql = "insert into todo (what, due) values ('" + wh + "', '" + du + "')"
	cur.execute(sql)
	conn.commit()
	# print("inserted")

	sql = "select * from todo where 1"
	cur.execute(sql)

	# 데이터를 패치합니다.
	rows = cur.fetchall()
	for row in rows:
		print(row)

	# 커넥션을 종료합니다.
	conn.close()
if __name__ == "__main__":
    sqlite_test()