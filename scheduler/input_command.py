from .valid_date import valid_date
from .make_string import make_string
from termcolor import colored
from pathlib import Path
import sqlite3


def print_calendar(year, month):
    import calendar
    c = calendar.TextCalendar(calendar.SUNDAY)
    string = c.formatmonth(year, month)
    print(string)


def done_percent(all, done):
    number_of_done = int(done * 100 / all)
    print(colored('>' * (number_of_done // 2), 'green') + colored('>' * ((100 - number_of_done)//2), 'red'))
    print("{}% Completed".format(number_of_done))


def input_command(command):
    home_dir = str(Path.home())
    if type(command) is str:
        command = command.split(' ')
    conn = sqlite3.connect(home_dir + "/scheduler.db")
    cur = conn.cursor()
    # 전체 도움말
    title_string = "%-35s|%-45s|%-40s\n"%("function", colored("command", 'yellow'), "example")
    add_help_string = ("-" * 35 + '+') + ("-" * 36 + '+') + ("-" * 30 + '+') + '\n'
    add_help_string += "%-35s|%-45s|%-40s\n"%("add schedule with category", colored("add {due} {content} in {category}", 'yellow'), colored("add 3/2 go school in school", 'cyan'))
    add_help_string += "%-35s|%-45s|%-40s\n"%("add schedule without category", colored("add {due} {content}", 'yellow'), colored("add 3/2 go school", 'cyan'))
    delete_help_string = ("-" * 35 + '+') + ("-" * 36 + '+') + ("-" * 30 + '+') + '\n'
    delete_help_string += "%-35s|%-45s|%-40s\n"%("delete all schedule", colored("delete all", 'yellow'), colored("delete all", 'cyan'))
    delete_help_string += "%-35s|%-45s|%-40s\n"%("delete schedule with index", colored("delete {index}", 'yellow'), colored("delete 3", 'cyan'))
    update_help_string = ("-" * 35 + '+') + ("-" * 36 + '+') + ("-" * 30 + '+') + '\n'
    update_help_string += "%-35s|%-45s|%-40s\n"%("update state with index", colored("update {index} {done/undone}", 'yellow'), colored("update 3 done", 'cyan'))
    update_help_string += "%-35s|%-45s|%-40s\n"%("update due date with index", colored("update {index} at {due}", 'yellow'), colored("update 3 at 7/1", 'cyan'))
    update_help_string += ("-" * 35 + '+') + ("-" * 36 + '+') + ("-" * 30 + '+') + '\n'
    update_help_string += "%-35s|%-45s|%-40s\n"%("update state with category", colored("update in {index} {done/undone}", 'yellow'), colored("update in school done", 'cyan'))
    update_help_string += "%-35s|%-45s|%-40s\n"%("update due date with category", colored("update in {index} at {due}", 'yellow'), colored("update in school at 7/1", 'cyan'))
    show_help_string = ("-" * 35 + '+') + ("-" * 36 + '+') + ("-" * 30 + '+') + '\n'
    show_help_string += "%-35s|%-45s|%-40s\n"%("get all schedule", colored("show all", 'yellow'), colored("show all", 'cyan'))
    show_help_string += "%-35s|%-45s|%-40s\n"%("get schedule with index", colored("show {index}", 'yellow'), colored("show 3", 'cyan'))
    show_help_string += "%-35s|%-45s|%-40s\n"%("get all schedule in category", colored("show in {category}", 'yellow'), colored("show in school", 'cyan'))
    show_help_string += "%-35s|%-45s|%-40s\n"%("get all schedule at month", colored("show in {month}", 'yellow'), colored("show at july", 'cyan'))
    show_help_string += "%-35s|%-45s|%-40s\n"%("get all schedule with state", colored("show {state}", 'yellow'), colored("show undone", 'cyan'))
    full_help_string = title_string + add_help_string + delete_help_string + update_help_string + show_help_string
    add_help_string = title_string + add_help_string
    delete_help_string = title_string + delete_help_string
    update_help_string = title_string + update_help_string
    show_help_string = title_string + show_help_string
    # 새 스케쥴 만드는 sql 구문
    insert_data = 'insert into todo (category, month, day, what, done) values (?,?, ?, ?, ?)'
    # 모든 스케쥴 삭제 sql 구문
    delete_all_data = 'drop table todo'
    # id로 스케쥴 삭제 sql 구문
    delete_data = 'delete from todo where id = ?'
    # 모든 스케쥴 선택 sql 구문
    select_data_all = 'select * from todo'
    select_data_all_done = 'select * from todo where done = 1'
    select_data_all_undone = 'select * from todo where done = 0'
    # id로 스케쥴 선택 sql 구문
    select_data = 'select * from todo where id=?'
    select_data_done = 'select * from todo where id=? and  done = 1'
    select_data_undone = 'select * from todo where id=? and  done = 1'
    # 카테고리로 스케쥴 선택 sql 구문
    select_data_cat = 'select * from todo where category=?'
    select_data_cat_done = 'select * from todo where category=? and done = 1'
    select_data_cat_undone = 'select * from todo where category=? and done = 0'
    # 월별로 스케쥴 선택 sql 구문
    select_data_mon = 'select * from todo where month=?'
    select_data_mon_done = 'select * from todo where month=? and done = 1'
    month_dic = {"January": 1, "january": 1, "Jan": 1, "jan": 1, "February": 2, "Feb": 2, "february": 2, "feb": 2, "March": 3, "march": 3,
                 "Mar": 3, "mar": 3, "April": 4, "april": 4, "Apr": 4, "apr": 4, "May": 5, "may": 5, "June": 6, "june": 6, "July": 7, "july": 7,
                 "August": 8, "august": 8, "Aug": 8, "aug": 8, "September": 9, "Sep": 9, "september": 9, "sep": 9, "October": 10, "Oct": 10,
                 "october": 10, "oct": 10, "November": 11, "Nov": 11, "november": 11, "nov": 11, "December": 12, "Dec": 12, "december": 12, "dec": 12}
    # id로 일정 업데이트 sql 구문
    update_data_by_id = 'update todo set done = ? where id = ?'
    update_data_by_id_due = 'update todo set month = ?, day = ? where id = ?'
    update_data_by_cat = 'update todo set done = ? where category = ?'
    update_data_by_cat_due = 'update todo set month = ?, day = ? where category = ?'
    if command[0] == 'add':
        if len(command) > 2:
            # 명령의 두번째 단어에 /가 없으면 날짜가 없는 것으로 간주하고, 추가하지 않는다.
            if '/' in command[1]:
                month, day = command[1].split('/')
                if not valid_date(int(month), int(day)):
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
                cur.execute(insert_data, (category, int(month), int(day), content, 0))
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
                cur.execute(delete_data, (int(command[1]),))
                conn.commit()
                print(command[1], "위치의 일정이 제거되었습니다.")
            # id로 된 일정이 없으면 예외처리
            except:
                print(delete_help_string.strip())
            cur.execute(select_data_all)
            result = cur.fetchall()
            print(make_string(result))
    elif command[0] == 'show':
        all_length = 0
        done_length = 0
        # 스케쥴 모두 보기
        if command[1] == 'all':
            cur.execute(select_data_all)
            result = cur.fetchall()
            all_length = len(result)
            print(make_string(result))
            cur.execute(select_data_all_done)
            done_length = len(cur.fetchall())
        # id로 스케쥴 검색
        elif command[1].isdigit():
            cur.execute(select_data, (command[1],))
            result = cur.fetchall()
            all_length = len(result)
            print(make_string(result))
            cur.execute(select_data_done, (command[1], ))
            done_length = len(cur.fetchall())
        # 카테고리로 스케쥴 검색
        elif command[1] == 'in':
            category = ''
            for x in command[2:]:
                category += x + ' '
            cur.execute(select_data_cat, (category.strip(),))
            result = cur.fetchall()
            all_length = len(result)
            print(make_string(result))
            conn.commit()
            cur.execute(select_data_cat_done, (category.strip(), ))
            done_length = len(cur.fetchall())
        elif command[1] == 'at':
            if command[2] in month_dic.keys():
                cur.execute(select_data_mon, (month_dic[command[2]],))
                result = cur.fetchall()
                all_length = len(result)
                print(make_string(result))
                cur.execute(select_data_mon_done, (month_dic[command[2]],))
                done_length = len(cur.fetchall())
            else:
                print("invalid month")
        elif command[1] == "done":
            cur.execute(select_data_all_done)
            result = cur.fetchall()
            print(make_string(result))
        elif command[1] == "undone":
            cur.execute(select_data_all_undone)
            result = cur.fetchall()
            print(make_string(result))
        elif (command[1] == 'calender' or command[1] == 'cal') and len(command) == 3:
            if '/' in command[2] and command[2].split("/")[0].isdigit() and command[2].split("/")[1].isdigit():
                if 70 < int(command[2].split("/")[0]) < 100:
                    year = int(command[2].split("/")[0]) + 1900
                elif 0 < int(command[2].split("/")[0]) <= 70:
                    year = int(command[2].split("/")[0]) + 2000
                else:
                    year = int(command[2].split("/")[0])
                print_calendar(year, int(command[2].split("/")[1]))
            else:
                print(show_help_string.strip())
        else:
            print(show_help_string.strip())
        if all_length != 0:
            done_percent(all_length, done_length)
    # 일정을 끝났는지 안끝났는지 명령어
    elif command[0] == 'update':
        # 두번째 키워드가 index이면,
        if command[1].isdigit():
            position = int(command[1])
            try:
                cur.execute(select_data, (position,))
                result = cur.fetchall()
            except:
                print('no schedule found')
                return 1
            if command[2] == 'done':
                print('index:', position, '\'s state is changed to done')
                cur.execute(update_data_by_id, (1, position,))
                conn.commit()
            elif command[2] == 'undone':
                print('index:', position, '\'s state is changed to undone')
                cur.execute(update_data_by_id, (0, position,))
                conn.commit()
            elif command[2] == 'at' and len(command) == 4 and '/' in command[3]:
                month, day = command[3].split('/')
                if not valid_date(int(month), int(day)):
                    print("Date is not valid")
                    return 1
                print('index:', position, '\'s due is changed to ' + command[3])
                cur.execute(update_data_by_id_due, (int(month), int(day), position,))
                conn.commit()
        # 두번째 키워드가 category이면,
        elif command[1] == 'in' and len(command) > 3:
            category = ''
            for x in category[2:]:
                category += x + ' '
            cur.execute(select_data_cat, (category.strip(),))
            result = cur.fetchall()
            if not result:
                print('no schedule found')
                return 1
            if command[3] == 'done':
                print('schedule in :', category, '\'s state is changed to done')
                cur.execute(update_data_by_cat, (1, category,))
                conn.commit()
            elif command[3] == 'undone':
                print('schedule in :', category, '\'s state is changed to undone')
                cur.execute(update_data_by_id, (0, category,))
                conn.commit()
            elif command[3] == 'at' and len(command) == 5 and '/' in command[4]:
                month, day = command[4].split('/')
                if not valid_date(int(month), int(day)):
                    print("Date is not valid")
                    return 1
                print('schedule in :', category, '\'s due is changed to ' + command[4])
                cur.execute(update_data_by_cat_due, (int(month), int(day), category,))
                conn.commit()
            else:
                print(update_help_string)
        # 아니면 update 도움말을 출력하도록 설정
        else:
            print(update_help_string)
            return 1
        conn.commit()
    elif command[0] == 'exit':
        return 1
    elif command[0] == 'help':
        print(full_help_string.strip())
    else:
        print('To get more info, plz input command \'help\'')
    conn.close()
    return 0
