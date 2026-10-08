

def inputs():
    num1=int(input('enter the num1:'))
    num2=int(input('enter the num2:'))
    cal=input('enter the calculation you want to  do:')
    return num1,num2,cal

def calculator(num1, num2, cal):
    if cal == "add":
        result = num1 + num2

    elif cal == "sub":
        result = num1 - num2

    elif cal == "mul":
        result = num1 * num2

    else:
        result = "invalid"

    return result

def run():
    try:
        num1,num2,cal=inputs()
        output= calculator(num1,num2,cal)
        print(output)

        print('next?')
    except Exception as e: 
        print(f'{e}')  


run()