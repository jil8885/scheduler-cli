from termcolor import colored
from .input_command import input_command
import sys


def main_scheduler():
    import sqlite3

    # SQLite DB파일을 생성하거나 연결합니다.
    conn = sqlite3.connect("scheduler.db")
    cur = conn.cursor()
    # table 만드는 sql 구문
    create_table = 'create table if not exists todo(id integer primary key autoincrement, category text not null, month integer not null, day integer not null, what text not null, done integer)'
    # 처음에 해당 테이블이 없을 때 테이블 생성 구문
    cur.execute(create_table)
    # 각종 도움말 메세지 문자열
    up_string = '\n'
    add_help_string = 'To add schedule, input \"add {} {} in {}\". You can omit \"in {}\".\n'.format(colored('{due(ex.3/2)}', 'yellow'), colored('{content}', 'yellow'), colored('{category}', 'yellow'), colored('{category}', 'yellow'))
    del_help_string = 'To delete schedule, input \"delete all\" or \"delete {}\".\n'.format(colored('{content}', 'yellow'))
    update_help_string = 'To update schedule, input \"update {} done\" or \"update {} undone\".\n'.format(colored('{index}', 'yellow'), colored('{index}', 'yellow'))
    check_help_string = 'To check schedule, input \"{}\" or \"{}\".\n'.format(colored('show all', 'yellow'), colored('show {index}', 'yellow'))
    exit_help_string = 'To exit, input \"{}\".\n'.format(colored('exit', 'yellow'))
    help_string = up_string + add_help_string + del_help_string + update_help_string + check_help_string + exit_help_string + up_string
    # exit을 입력받을 때까지 계속 입력
    if len(sys.argv) == 1:
        # 초기 도움말 메세지 1회 출력
        print(help_string)
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
