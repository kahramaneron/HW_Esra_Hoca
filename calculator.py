op_quantity = int(input("How many times will you make op: "))    
op_count = 1

while op_quantity >= op_count:
    first_number = int(input("Enter a number: "))
    operation = input("Enter type of op(+,-,*,/): ")
    second_number = int(input("Enter a number: "))
    op_count += 1

    
    if operation == '+':
            print('result is: ', first_number + second_number)
    elif operation == '*':
            print('result is: ', first_number * second_number)
    elif operation == '/':
            print('result is: ', first_number / second_number)
    else:
            print('result is: ', first_number - second_number)

