import datetime

def display_current_datetime():
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d %H:%M")

def calculate_future_date(days_to_add):
    current_date = datetime.date.today()
    future_date = current_date + datetime.timedelta(days=days_to_add)
    return future_date.strftime("%Y-%m-%d")

if __name__ == '__main__':
    print("Current date and time:", display_current_datetime())
    
    days = input("Enter number of days to add: ")
    
    if days.isdigit():
        days = int(days)
        print("Future date:", calculate_future_date(days))
    else:
        print("Please enter a valid number.")
