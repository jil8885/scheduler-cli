def main_scheduler():
    import sqlite3

    # SQLite DB파일을 생성하거나 연결합니다.
    conn = sqlite3.connect("scheduler.db")
    cur = conn.cursor()
    create_table = 'create table if not exists todo(id integer primary key autoincrement, categoty text not null, due text not null, what text not null, done integer);'
    insert_data = 'insert into todo (what, due) values (?,?)'
    cur.execute(create_table)
    while True:
        # 입력을 문장으로 받는다.
        command = input().split(' ')
        # 첫번째 단어가 add 일 때, db에 일정을 추가한다.
        if command[0] == 'add':
            # 명령의 두번째 단어에 /가 없으면 날짜가 없는 것으로 간주하고, 추가하지 않는다.
            if '/' in command[1]:
                month, day = command[1].split('/')
                # in 키워드를 통해 어느 분류에 넣을지 정할 수 있다.
                try:
                    category_split = command.index('in')
                    category = command[category_split + 1]
                    content_list = command[category_split + 2:]
                # in 키워드가 없으면 미분류 처리한다.
                except:
                    category = 'No category'
                    content_list = command[2:]
            print(month, day, category)
            content = ''
            for x in content_list:
                content += x + ' '
            content = content.strip()
            print(content)
            break
#    cur.execute(insert_data, (what, due, ))
    conn.commit()
    cur.close()
    conn.close()


if __name__ == "__main__":
    main_scheduler()