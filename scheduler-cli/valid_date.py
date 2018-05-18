# 일정 추가시 유효한 날짜인지 구별하는 함수
def valid_date(month, day):
    month31 = [1, 3, 5, 7, 8, 10, 12]
    month30 = [4, 6, 9, 11]
    return (month in month31 and day > 0 and day < 32) or (month in month30 and day > 0 and day < 31) or (month == 2 and day > 0 and day < 29)
