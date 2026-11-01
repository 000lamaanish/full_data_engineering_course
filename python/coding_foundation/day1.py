# sum
import math
a=int(input('enter the first number:'))
b=int(input('enter the second number:'))

def add(a,b):
    sum=a+b
    return sum

output=add(a,b)
print(f'{output}')


def evenodd(num):
    if num %2==0:
        print('even')
    elif num %2 != 0:
        print('odd')
    else:
        print('zero')

evenodd(a)
evenodd(b)
