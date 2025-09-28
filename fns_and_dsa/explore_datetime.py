import datetime

def display_current_datetime():
    now = datetime.datetime.now()
    formatted_date_time = now.strftime("%Y-%m-%d %H:%M:%S")
    return formatted_date_time

def calculate_future_date(days_to_add=7):
    current_date = datetime.date.today()
    future_date = current_date + datetime.timedelta(days=days_to_add)
    return future_date.strftime("%Y-%m-%d")

if __name__ == '__main__':
    print(display_current_datetime())
    print(calculate_future_date(10))
