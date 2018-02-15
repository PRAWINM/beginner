year=int(input("Enter year to be checked:"))
if(year%4==0 and year%100!=0 or year%400==0):
    print("YES this year is a leap year!")
else:
    print("NO this year is not a leap year!")
