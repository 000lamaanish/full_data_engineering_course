

# def inputs():
#     num1=int(input('enter the num1:'))
#     num2=int(input('enter the num2:'))
#     cal=input('enter the calculation you want to  do:')
#     return num1,num2,cal

# def calculator(num1, num2, cal):
#     if cal == "add":
#         result = num1 + num2

#     elif cal == "sub":
#         result = num1 - num2

#     elif cal == "mul":
#         result = num1 * num2

#     else:
#         result = "invalid"

#     return result

# def run():
#     try:
#         num1,num2,cal=inputs()
#         output= calculator(num1,num2,cal)
#         print(output)

#         print('next?')
#     except Exception as e: 
#         print(f'{e}')  


# run()

# projects 1: expenses tracker

expences =[]
total=0
def add_expences():
    expense_name=input("enter the name of the expenditure:")
    amount=int(input(f"enter the amount of {expense_name}:"))
    expences.append((expense_name,amount))
    return expences
# print(expenses)

def listed_names(expenses):
    for name, amount in expenses:
        print(f'{name}:{amount}')


def total_amount():
    total=0
    for name, amount in expences:
        total+=amount
        print("total expences:",total)


add_expences()
add_expences()
listed_names(expences)   
total_amount()        