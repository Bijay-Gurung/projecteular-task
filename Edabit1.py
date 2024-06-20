import datetime

def time_for_milk_and_cookies(date):
    if date.strftime("%m")=="12" and date.strftime("%d")=="24":
        return True
    else:
        return False

print(time_for_milk_and_cookies(datetime.date(2024,12,24)))
print(time_for_milk_and_cookies(datetime.date(2024,12,23)))
print(time_for_milk_and_cookies(datetime.date(2024,1,24)))

