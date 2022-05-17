from datetime import datetime


def get_str_date(date):
    date = date.replace("Z", "")
    d = datetime.fromisoformat(date)
    str_date = datetime.strftime(d, "%A %d %B %Y")
    print(str_date)
    return str_date


get_str_date("2021-05-27 17:08:34.149Z")