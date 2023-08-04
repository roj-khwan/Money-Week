import datetime
import math

#region setting
start_date = datetime.date(2023, 2, 8)
end_date = datetime.date(2024, 2, 7)
current_date = datetime.date.today()
# current_date = datetime.date(2023, 2, 15)

moneyGoal = 639

# start at Monday (1) -> Sunday (7)
target_weekday = 7

currency = "Baht"
#endregion setting

def ordinal(number):
    if 10 <= number % 100 <= 20:
        suffix = 'th'
    else:
        suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(number % 10, 'th')

    return f"{number}{suffix}"

if __name__ == '__main__':
    # Check if dates make sense
    if start_date > current_date:
        print('Current Date is Before Start Date')
        exit()

    if start_date > end_date:
        print('End Date is Before Start Date')
        exit()

    if current_date > end_date:
        print('End Date is Before Current Date')
        exit()

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

    print(f"Weeks between Start - End: {start_end_week_diff} Week{'s' if start_end_week_diff != 1 else ''}")
    print(f"Current Week: {ordinal(start_current_week_diff)} Week{'s' if start_current_week_diff != 1 else ''}")
    print(f"Amount of money you should've by now: {math.ceil(start_current_week_diff * money_per_week)} {currency}")
    print(f"You should collect money every week for: {math.ceil(money_per_week)} {currency}")