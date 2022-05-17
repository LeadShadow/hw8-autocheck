from datetime import date
import calendar


def get_days_in_month(month, year):
    return calendar.monthrange(year, month)[1]