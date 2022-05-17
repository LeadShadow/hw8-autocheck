from datetime import datetime


def get_days_from_today(date):
    list = []
    date_1 = date.split("-")
    date_now = datetime.now()
    for i in date_1:
        i = int(i)
        list.append(i)
    date_2 = datetime(year=list[0], month=list[1], day=list[2])
    result = date_now - date_2
    return result.days


print(get_days_from_today('2020-10-09'))