from datetime import datetime, timedelta

def calculate_date(date_str, n):
    date_format = "%y-%m-%d"
    date = datetime.strptime(date_str, date_format)
    new_date = date + timedelta(days=n)
    new_date_str = new_date.strftime(date_format)
    return new_date_str
