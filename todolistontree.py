class Node:#tree <parent, children>
	def __init__(self, _par):
		super(Node, self).__init__()
		self.parent = _par
		self.children = []

	def setParent(self, x):
		self.parent = x

	def showParent(self):
		print(self.parent)

	def addChild(self, x):
		import bisect
		bisect.insort(self.children, x)

	def delChild(self, x):
		self.children.remove(x)

def create_db():
	import sqlite3
	conn = sqlite3.connect("lab.db") #DB file connect
	cur = conn.cursor() #DB file cursor

	table_create_sql = """create table if not exists todo (
				id integer primary key autoincrement,
				what text not null,
				due text not null,
				finished integer,
				parent integer);"""
	cur.execute(table_create_sql) #creat table

	cur.execute('''SELECT * from todo where 1''')
	rows = cur.fetchall()

	conn.close() #connect close

def create_tree():
	tree.append(Node(-1))
	import sqlite3
	conn = sqlite3.connect("lab.db") #DB file connect
	cur = conn.cursor() #DB file cursor

	i = 1
	cur.execute('''SELECT * from todo where 1''')
	rows = cur.fetchall() #data fetch on sentence
	
	for row in rows:
		while i<row[0]:
			tree.append(0)
			i = i+1
		tree.append(Node(row[4]))
		tree[row[4]].addChild(row[0])
		i = i+1

	conn.close()

def add_todo():
	import sqlite3
	conn = sqlite3.connect("lab.db") #DB file connect
	cur = conn.cursor() #DB file cursor

	wh = input("Todo? ")
	du = input("Due date? ")
	par = int(input("what parent? "))
	cur.execute('''INSERT INTO todo (what, due, finished, parent) values (?, ?, 0, ?)''', (wh, du, par))

	conn.commit() #DB file modify on sentence
	conn.close() #connect close

def list_todo():
	import sqlite3
	conn = sqlite3.connect("lab.db") #DB file connect
	cur = conn.cursor() #DB file cursor

	cur.execute('''SELECT * from todo where 1''')
	rows = cur.fetchall() #data fetch on sentence

	for row in rows:
		print(row)

	conn.close() #connet close

def delete_todo():
	import sqlite3
	conn = sqlite3.connect("lab.db")
	cur = conn.cursor()

	Rid = int(input("Delete id? "))

	cur.execute('''DELETE FROM todo WHERE ID = ?''', (Rid,))
	conn.commit() #DB file modify on sentence
	conn.close() #connet close