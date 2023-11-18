# Python3 code to calculate age in years
from datetime import date


def calculate_age(birthdate):
    days_in_year = 365.2425
    age = int((date.today() - birthdate).days / days_in_year)
    return age


# Driver code
born = input("Please Enter your birthdate:")
year = int(born.split("/")[0])
month = int(born.split("/")[1])
day = int(born.split("/")[2])
if year<1 or year>date.today().year:
    print("Year is Wrong")
elif month<1 or month>12:
    print("Month is Wrong")
elif day<1 or day>31:
    print("Day is Wrong")
else:
    print(calculate_age(date(year, month, day)), "years")
