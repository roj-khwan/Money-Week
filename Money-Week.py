import datetime
import math

#region setting
start_date = None
end_date = None
current_date = None

moneyGoal = None

# start at Monday (1) -> Sunday (7)
target_weekday = 7

currency = "USD"
#endregion setting

def ordinal(number):
    if 10 <= number % 100 <= 20:
        suffix = 'th'
    else:
        suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(number % 10, 'th')

    return f"{number}{suffix}"

if __name__ == '__main__':
    # User Input
    date_raw = input("Please Input Start Date (YYYY/MM/DD) : ").strip().split('/')
    while not start_date:
        try:
            y, m, d = map(int, date_raw)
            start_date = datetime.date(y, m, d)
        except:
            print("Error 1: Look like It's an Invalid Input.\nPlease reEnter Start Date According to Format. (YYYY/MM/DD)")
            date_raw = input("Please Input Start Date (YYYY/MM/DD) : ").strip().split('/')

    date_raw = input("Please Input End Date (YYYY/MM/DD) : ").strip().split('/')
    while not end_date:
        try:
            y, m, d = map(int, date_raw)
            end_date = datetime.date(y, m, d)

            if start_date >= end_date:
                print("Error 2:End Date can't be before Start Date")
                end_date = None

        except:
            print("Look like It's an Invalid Input.\nPlease reEnter End Date According to Format. (YYYY/MM/DD)")
            date_raw = input("Please Input End Date (YYYY/MM/DD) : ").strip().split('/')

    date_raw = input("Please Input Current Date (YYYY/MM/DD) : ").strip().split('/')
    while not current_date:
        try:
            y, m, d = map(int, date_raw)
            current_date = datetime.date(y, m, d)

            if start_date > current_date:
                print("Error 2:Current Date can't be before Start Date")
                current_date = None
            if current_date >= end_date:
                print("Error 2:Current Date can't be after End Date")
                current_date = None
                
        except:
            print("Look like It's an Invalid Input.\nPlease reEnter Current Date According to Format. (YYYY/MM/DD)")
            date_raw = input("Please Input Current Date (YYYY/MM/DD) : ").strip().split('/')

    money_raw = input("Please Input Expected Money : ")
    try:
        moneyGoal = abs(int(money_raw))
    except:
        print("Please Input Invalid amount of money")
        money_raw = input("Please Input Expected Money : ")


    # Nearest weekday to closest target weekday
    # Current and end date are closest previous weekday
    # But start date is next weekday
    current_date_weekday = current_date - datetime.timedelta(current_date.weekday() + 1)
    end_date_weekday = end_date - datetime.timedelta(end_date.weekday() + 1)
    start_date_weekday = datetime.timedelta(target_weekday - (start_date.weekday() + 1)) + start_date

    # Calculate weeks between start->end and start->current
    start_end_week_diff = ((end_date_weekday - start_date_weekday) / 7).days + 1
    start_current_week_diff = ((current_date_weekday - start_date_weekday) / 7).days + 1

    money_per_week = moneyGoal / start_end_week_diff

    print('-' * 13)
    print(f"Weeks between Start - End: {start_end_week_diff} Week{'s' if start_end_week_diff != 1 else ''}")
    print(f"Current Week: {ordinal(start_current_week_diff)} Week{'s' if start_current_week_diff != 1 else ''}")
    print(f"Amount of money you should've by now: {math.ceil(start_current_week_diff * money_per_week)} {currency}")
    print(f"You should collect money every week for: {math.ceil(money_per_week)} {currency}")