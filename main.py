def isvaliddate(month, day):
    month31 = [1, 3, 5, 7, 8, 10, 12]
    month30 = [4, 6, 9, 11]
    return (month in month31 and day > 0 and day < 32) or (month in month30 and day > 0 and day < 31) or (month == 2 and day > 0 and day < 29)

def main_scheduler():
    import sqlite3, sys

    # SQLite DB파일을 생성하거나 연결합니다.
    conn = sqlite3.connect("scheduler.db")
    cur = conn.cursor()
    create_table = 'create table if not exists todo(id integer primary key autoincrement, category text not null, due text not null, what text not null, done integer);'
    insert_data = 'insert into todo (category, due, what, done) values (?,?, ?, ?)'
    delete_all_data = 'drop table todo'
    cur.execute(create_table)
    while True:
        # 입력을 문장으로 받는다.
        command = input('Input a command: ').split(' ')
        cur.execute(create_table)
        # 첫번째 단어가 add 일 때, db에 일정을 추가한다.
        if command[0] == 'add':
            if len(command) > 2:
                # 명령의 두번째 단어에 /가 없으면 날짜가 없는 것으로 간주하고, 추가하지 않는다.
                if '/' in command[1]:
                    month, day = command[1].split('/')
                    if not isvaliddate(int(month), int(day)):
                        print('유효한 날짜가 아닙니다.')
                        continue
                    # in 키워드를 통해 어느 분류에 넣을지 정할 수 있다.
                    try:
                        category_split = command.index('in')
                        category_list = command[category_split + 1:]
                        content_list = command[2:category_split]
                    # in 키워드가 없으면 미분류 처리한다.
                    except:
                        category = 'No category'
                        content_list = command[2:]
                    content = ''
                    for x in content_list:
                        content += x + ' '
                    category = ''
                    for x in category_list:
                        category += x + ' '
                    category = category.strip()
                    cur.execute(insert_data, (category, month + '/' + day, content, 0))
                    print(month + '월' + day + '일에 ' + content +' 일정이 ' + category + '분류에 저장되었습니다.')
                    conn.commit()
                else:
                    print('명령어에 날짜가 없습니다.')
            else:
                print('일정을 추가하시려면 add 3/2 {내용} in {분류} 순으로 입력해주세요. in {분류}는 생략할 수 있습니다')
        elif command[0] == 'delete':
            try:
                if command[1] == 'all':
                    cur.execute(delete_all_data)
                    conn.commit()
            except:
                print('일정을 제거하시려면 delete all 또는 delete {숫자} 형식으로 입력해주세요')
        elif command[0] == 'exit':
            sys.exit()
    cur.close()
    conn.close()


if __name__ == "__main__":
    main_scheduler()