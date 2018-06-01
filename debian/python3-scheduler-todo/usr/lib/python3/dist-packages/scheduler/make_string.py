from termcolor import colored
from colorama import init
from datetime import datetime
# 검색 후 결과 문자열 만드는 함수


def make_string(schedule_list):
    init()
    string = 'due\t\t|content\t\t|category\t|done\n'
    string += '-' * 80 + '\n'
    done = ['undone', 'done', 'overdue']
    color = ['yellow', 'green', 'red']
    if not schedule_list:
        string += 'No result found. To show all schedule, enter \"show all\"'
    for x in schedule_list:
        overdue = datetime(x[0], x[2], x[3]) - datetime.now()
        if overdue.days < 0 and x[5] == 0:
            a = 2
        else:
            a = x[5]
        string += '%-15s |%-22s |%-14s |%-15s\n'%(str(x[0]) +'/' + str(x[2]) + '/' + str(x[3]), x[4], x[1], colored(done[a], color[a]))
    return string.strip()