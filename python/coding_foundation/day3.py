# Write a Python program that prints numbers from 1 to 50 using a for loop.
for i in range(1,51):
    print(i)
    i+=1



# 4
n=int(input("enter the number:"))
for i in range(1,11):
    multiplication=n*i
    print(f'{n}*{i}={multiplication}')

# 2
for i in range(1,101):
    if i%2==0:
        print(i)
    i=i+1    

# 3
n=int(input("enter the natural number:"))
i=1
sum=0

while i<=n:
    sum=sum+i
    i=i+1
print(sum)

