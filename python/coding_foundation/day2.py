# largest number

a=2
b=4
c=3

def numsize(a,b,c):
    if a>b and a>c:
        print('a is the largest')
    elif b>a and b>c:
        print('b is largest')
    else:
        print('c is largest') 

numsize(a,b,c)


# grade calcullator

marks=int(input('enter the marks of a student:'))

def grade_callculator(marks):
    if marks >= 90 and marks==100:
        print('A')
    elif marks >=80:
        print('B')
    elif marks >70:
        print('c')
    elif marks>=60:
        print('D')
    else:
        print("F")
grade_callculator(marks)                        


# leap year finder
year=int(input('enter the year:'))
def lep_year_calcuator(a):
    if (a%400==0) or (a%4==0 and a%100!=0):
        print('lep year')
    else:
        print('nomal year')

lep_year_calcuator(year)