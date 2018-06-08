from termcolor import colored
from colorama import init
from .input_command import input_command
import sys
from pathlib import Path


def main_scheduler():
    init()
    import sqlite3
    home_dir = str(Path.home())
    # SQLite DB파일을 생성하거나 연결합니다.
    conn = sqlite3.connect(home_dir + "/scheduler.db")
    cur = conn.cursor()
    # table 만드는 sql 구문
    create_table = 'create table if not exists todo(year integer not null, category text not null, month integer not null, day integer not null, what text not null, done integer)'
    # 처음에 해당 테이블이 없을 때 테이블 생성 구문
    cur.execute(create_table)
    # 각종 도움말 메세지 문자열
    # 전체 도움말
    title_string = "%-35s|%-36s|%-40s\n"%("function", "command", "example")
    add_help_string = ("-" * 35 + '+') + ("-" * 36 + '+') + ("-" * 30 + '+') + '\n'
    add_help_string += "%-35s|%-45s|%-40s\n"%("add schedule with category", colored("add {due} {content} in {category}", 'yellow'), colored("add 2018/3/2 go school in school", 'cyan'))
    add_help_string += "%-35s|%-45s|%-40s\n"%("add schedule without category", colored("add {due} {content}", 'yellow'), colored("add 2018/3/2 go school", 'cyan'))
    delete_help_string = ("-" * 35 + '+') + ("-" * 36 + '+') + ("-" * 30 + '+') + '\n'
    delete_help_string += "%-35s|%-45s|%-40s\n"%("delete all schedule", colored("delete all", 'yellow'), colored("delete all", 'cyan'))
    delete_help_string += "%-35s|%-45s|%-40s\n"%("delete schedule with category", colored("delete in {category}", 'yellow'), colored("delete in hoesung", 'cyan'))
    delete_help_string += "%-35s|%-45s|%-40s\n"%("delete schedule with index", colored("delete {content}", 'yellow'), colored("delete hit hoesung", 'cyan'))
    update_help_string = ("-" * 35 + '+') + ("-" * 36 + '+') + ("-" * 30 + '+') + '\n'
    update_help_string += "%-35s|%-45s|%-40s\n"%("update state with index", colored("update {content} {done/undone}", 'yellow'), colored("update hit hoesung done", 'cyan'))
    update_help_string += "%-35s|%-45s|%-40s\n"%("update due date with index", colored("update {content} at {due}", 'yellow'), colored("update hit hoesung at 2018/7/1", 'cyan'))
    update_help_string += ("-" * 35 + '+') + ("-" * 36 + '+') + ("-" * 30 + '+') + '\n'
    update_help_string += "%-35s|%-45s|%-40s\n"%("update state with category", colored("update in {category} {done/undone}", 'yellow'), colored("update in school done", 'cyan'))
    update_help_string += "%-35s|%-45s|%-40s\n"%("update due date with category", colored("update in {category} at {due}", 'yellow'), colored("update in school at 2018/7/1", 'cyan'))
    show_help_string = ("-" * 35 + '+') + ("-" * 36 + '+') + ("-" * 30 + '+') + '\n'
    show_help_string += "%-35s|%-45s|%-40s\n"%("get all schedule", colored("show all", 'yellow'), colored("show all", 'cyan'))
    show_help_string += "%-35s|%-45s|%-40s\n"%("get schedule with index", colored("show {content}", 'yellow'), colored("show hit hoesung", 'cyan'))
    show_help_string += "%-35s|%-45s|%-40s\n"%("get all schedule in category", colored("show in {category}", 'yellow'), colored("show in school", 'cyan'))
    show_help_string += "%-35s|%-45s|%-40s\n"%("get all calender at specific month", colored("show cal {year/month}", 'yellow'), colored("show cal 2018/03", 'cyan'))
    full_help_string = title_string + add_help_string + delete_help_string + update_help_string + show_help_string
    add_help_string = title_string + add_help_string
    show_help_string = title_string + show_help_string
    update_help_string = title_string + update_help_string
    delete_help_string = title_string + delete_help_string
    # exit을 입력받을 때까지 계속 입력
    if len(sys.argv) == 1:
        # 초기 도움말 메세지 1회 출력
        print(full_help_string)
        while True:
            # 입력을 문장으로 받는다.
            command = input('Input a command: ')
            if input_command(command) == 1:
                break
    else:
        input_command(sys.argv[1:])
    cur.close()
    conn.close()


if __name__ == "__main__":
    main_scheduler()
