# Write a program to generate student results.

Sno=int(input('Enter Student Number:'))
Sname=input('Enter Student Name:')
Group=input('Enter group:')
s1=int(input('Enter English Marks:'))
s2=int(input('Enter Computer Marks:'))
s3=int(input('Enter Maths Marks:'))
tot=s1+s2+s3
avg=tot/3
if avg>=90:
    print('First Class')
elif avg>=70:
    print('Second Class')
elif avg>=50:
    print('Third Class')
else:
    print('Pass')
