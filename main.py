from termcolor import colored
# 일정 추가시 유효한 날짜인지 구별하는 함수
def isvaliddate(month, day):
    month31 = [1, 3, 5, 7, 8, 10, 12]
    month30 = [4, 6, 9, 11]
    return (month in month31 and day > 0 and day < 32) or (month in month30 and day > 0 and day < 31) or (month == 2 and day > 0 and day < 29)

# 검색 후 결과 문자열 만드는 함수
def make_string(schedule_list):
    string = 'id\t|due\t\t|content\t\t|category\t|done\n'
    string += '-' * 80 + '\n'
    done = ['undone', 'done']
    color = ['red', 'green']
    if schedule_list == []:
        string += 'No result found. To show all schedule, enter \"show all\"'
    for x in schedule_list:
        string += '%-7s |%-14s |%-22s |%-14s |%-15s\n'%(str(x[0]), x[2], x[3], x[1], colored(done[x[4]], color[x[4]]))
    return string.strip()

def printCalendar(year, month):
	import calendar
	c = calendar.TextCalendar(calendar.SUNDAY)
	str = c.formatmonth(year, month)
	print(str)
    
def main_scheduler():
    import sqlite3, sys

    # SQLite DB파일을 생성하거나 연결합니다.
    conn = sqlite3.connect("scheduler.db")
    cur = conn.cursor()
    # table 만드는 sql 구문
    create_table = 'create table if not exists todo(id integer primary key autoincrement, category text not null, due text not null, what text not null, done integer);'
    # 새 스케쥴 만드는 sql 구문
    insert_data = 'insert into todo (category, due, what, done) values (?,?, ?, ?)'
    # 모든 스케쥴 삭제 sql 구문
    delete_all_data = 'drop table todo'
    # id로 스케쥴 삭제 sql 구문
    delete_data = 'delete from todo where id = ?'
    # 모든 스케쥴 선택 sql 구문
    select_data_all = 'select * from todo'
    # id로 스케쥴 선택 sql 구문
    select_data = 'select * from todo where id=?'
    # 카테고리로 스케쥴 선택 sql 구문
    select_data_cat = 'select * from todo where category=?'
    # id로 일정 업데이트 sql 구문
    update_data_by_id = 'update todo set done = ? where id = ?'
    # 처음에 해당 테이블이 없을 때 테이블 생성 구문
    cur.execute(create_table)
    # 각종 도움말 메세지 문자열
    add_help_string = 'To add schedule, input \"add 3/2 {content} in {category}\". You can omit \"in {category}\".\n'
    del_help_string = 'To delete schedule, input \"delete all\" or \"delete {index}\".\n'
    update_help_string = 'To update schedule, input \"update {index} done\" or \"update {index} undone\".\n'
    check_help_string = 'To check schedule, input \"show all\" or \"show {index}\".\n'
    exit_help_string = 'To exit, input \"exit\".'
    help_string = add_help_string + del_help_string + update_help_string + check_help_string + exit_help_string
    # 초기 도움말 메세지 1회 출력
    print(help_string)
    # exit을 입력받을 때까지 계속 입력
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
                    # in 키워드를 통해 어느 category에 넣을지 정할 수 있다.
                    try:
                        category_split = command.index('in')
                        category_list = command[category_split + 1:]
                        content_list = command[2:category_split]
                    # in 키워드가 없으면 미category 처리한다.
                    except:
                        category = 'No category'
                        content_list = command[2:]
                    # content, category를 띄어쓰기로 묶기
                    content = ''
                    for x in content_list:
                        content += x + ' '
                    if len(content) > 22:
                        print("plz enter content less than 20 letters")
                        continue
                    category = ''
                    for x in category_list:
                        category += x + ' '
                    category = category.strip()
                    cur.execute(insert_data, (category, month + '/' + day, content, 0))
                    print('schedule ' + content + ' in ' + category + ' at ' + command[1])
                    conn.commit()
                # 명령어에 날짜가 없는 경우 다시 입력 받기
                else:
                    print('There is no date in command')
            # 날짜도 없으면 스케쥴 추가 문자열 출력
            else:
                print(add_help_string.strip())
        elif command[0] == 'delete':
            # 모두 스케쥴 삭제
            if command[1] == 'all':
                cur.execute(delete_all_data)
                conn.commit()
            # id로 스케쥴 찾아서 삭제
            else:
                try:
                    cur.execute(delete_data,(int(command[1]),))
                    conn.commit()
                # id로 된 일정이 없으면 예외처리
                except:
                    print(del_help_string.strip())
        elif command[0] == 'show':
            try:
                # 스케쥴 모두 보기
                if command[1] == 'all':
                    cur.execute(select_data_all)
                    result = cur.fetchall()
                    print(make_string(result))
                # id로 스케쥴 검색
                elif command[1].isdigit():
                    cur.execute(select_data, (command[1],))
                    result = cur.fetchall()
                    print(make_string(result))
                # 카테고리로 스케쥴 검색
                else:
                    cur.execute(select_data_cat, (command[1],))
                    result = cur.fetchall()
                    print(make_string(result))
                    conn.commit()                    
            except:
                print(check_help_string.strip())
        # 일정을 끝났는지 안끝났는지 명령어
        elif command[0] == 'update':
            # 두번째 키워드가 index이면,
            try:
                position = int(command[1])
            # 아니면 update 도움말을 출력하도록 설정
            except:
                print(update_help_string)
                continue
            try:
                cur.execute(select_data, (position,))
                result = cur.fetchall()
            except:
                print('no schedule found')
                continue
            if command[2] == 'done':
                print('index:', position, '\'s state is changed to done')
                cur.execute(update_data_by_id, (1, position,))
                conn.commit()
            elif command[2] == 'undone':
                print('index:', position, '\'s state is changed to undone')
                cur.execute(update_data_by_id, (0, position,))
                conn.commit()
            else:
                print(update_help_string)
            conn.commit()
        elif command[0] == 'exit':
            sys.exit()
        elif command[0] == 'help':
            print(help_string.strip())
        else:
            print('To get more info, plz input command \'help\'')
    cur.close()
    conn.close()



if __name__ == "__main__":
    main_scheduler()
