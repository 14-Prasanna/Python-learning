month = int(input())
year = int(input())
months = ["January","February","March","April","May","June",
          "July","August","September","October","November","December"]
month_name = months[month - 1]
if month in [1,3,5,7,8,10,12]:
    days = 31
elif month in [4,6,9,11]:
    days = 30
elif month == 2:
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        days = 29
    else:
        days = 28
print(month_name, year, "has", days, "days")