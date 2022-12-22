print("Q2")
print()
print("Enter Date below to get date of next day.\n")


def leapyear(x):
    if (x%400)==0 or ((x%100!=0) and (x%4==0)):
        return True
    else:
        return False


date=int(input("Enter Date [1-31]:"))
month=int(input("Enter Month [1-12]:"))
year=int(input("Enter Year [1800-2025]:"))


if date<1 or date>31 or month<1 or month>12 or year<1800 or year>2025:
    condition1=False
else:
    condition1=True


month_31 = [1, 3, 5, 7, 9, 11]
month_30 = [4, 6, 8, 10, 12]


a= date == 31 and (month in month_30)


c1b= date > 29 and month == 2


c1c= date == 29 and (not leapyear(year)) and month == 2
if a or c1b or c1c :
    condition2=False
else:
    condition2=True



if a:
    print(f"\nError\n{date} day can't be in month {month}")
elif c1b:
    print(f"\nError\n{date} day can't be in month {month}")
elif c1c:
    print(f"\nError\n{date} day can't be in month {month} as the year {year} in not leapyear")
elif condition1==False:
    print(f"\nError\nPlease enter date in range day[1-31], month[1-12], year[1800-2025] ")



if condition1==True and condition2==True :
    month_31 = [1, 3, 5, 7, 9, 11]
    month_30 = [4, 6, 8, 10, 12]

    if (month in month_31) == True:
        if date == 31:
            date = 1
            month = month + 1
        elif 1 <= date <= 30:
            date = date + 1

    elif (month in month_30) == True:
        if date == 30 and month == 12:
            date = 1
            month = 1
            year = year + 1
        elif date == 30 and month != 12:
            date = 1
            month = month + 1
        elif 1 <= date <= 29:
            date = date + 1

    elif month == 2:

        if leapyear(year) == True:
            if date == 29:
                date = 1
                month = month + 1
            elif 1 <= date <= 28:
                date = date + 1

        elif leapyear(year) == False:
            if date == 28:
                date = 1
                month = month + 1
            elif 1 <= date <= 27:
                date = date + 1

    print(f"\nNext Date in format Day/Month/Year is: {date}/{month}/{year}")