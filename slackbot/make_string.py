from datetime import datetime
# 검색 후 결과 문자열 만드는 함수


def make_string(schedule_list):
    done = ['undone', 'done', 'overdue']
    string = '%-35s %-22s %-12s %-21s%-10s\n'%('Due' , 'Content', 'Category', 'Finished', 'D-day')
    if not schedule_list:
        string += 'No result found. To show all schedule, enter \"show all\"'
    for x in schedule_list:
        x = x[1:]
        overdue = datetime(x[0], x[2], x[3]) - datetime.now()
        if overdue.days < 0:
            if x[5] == 0:
                a = 2
            else:
                a = x[5]
            dday = 'D+' + str((-1) * overdue.days)
        else:
            a = x[5]
            dday = 'D' + str((-1) * overdue.days)
        if x[3] > 9:
            day = str(x[3])
        else:
            day = '0' + str(x[3])
        if x[2] > 9:
            month = str(x[2])
        else:
            month = '0' + str(x[2])
        date = datetime(x[0], x[2], x[3]).weekday()
        weekdays = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
        string += '%-25s %-22s %-14s %-20s%-10s\n'%(str(x[0]) +'/' + month + '/' + day + '(' + weekdays[date] + ')' , x[4], x[1], done[a], dday)
    return string.strip()