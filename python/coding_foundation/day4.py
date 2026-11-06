# nested loops

# for i in range(1,4):
#     for j in range(1,3):
#         print (i,j)



# for i in range(1,4):
#     for j in range(1, i+1):
#         print(j,end=" ")
# #     print()    

# # for i in range(1,5):
# #     for j in range(1,i+1):
# #         print(j,end=" ")
# #     print()    

# # for i in range (1,4):


# # for i in range(1, 4):
# #     for j in range(1, 4):
# #         print("*", end=" ")
# #     print()


# # for i in range(1,10):
# #     for j in range(1,i+1):
# #         print("#", end='')
# #     print()       


# for i in range(5,1,-1):
#     for j in range(1,i+1):
#         print(i, end='')
#     print()           

# for i in range(1,6):
#     for j in range(5,5-i,-1):
#         print(j, end='')
#     print()           

# import math
# x=int(input("enter the number:"))
# list=[]
# for i in range(x,0,-1):
#     list.append(i)
# print(math.prod(list))

import math
num=int(input("enter the number:"))
print(math.factorial(num))    

print(math.sum(num))