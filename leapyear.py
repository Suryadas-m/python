year = int(input("Enter a year: "))
if (year % 400 == 0) and (year % 100 == 0):
    print("given year is a leap year")
elif (year % 4 ==0) and (year % 100 != 0):
    print("given year is a leap year")
else:
    print("given year is not a leap year")
