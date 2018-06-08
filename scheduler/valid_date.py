# 일정 추가시 유효한 날짜인지 구별하는 함수
def valid_date(year, month, day):
	valMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
		valMonth[1] = 29
	return 0 < month and month <= 12 and 0 < day and day <= valMonth[month-1]
