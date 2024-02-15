# Write a program to print given year is a Leap year or not.

year=int(input('Enter a Year:'))
if year%4==0 or year%100!=0 and year%400==0:
    print('Leap Year')
else:
    print('Not a Leap Year')
