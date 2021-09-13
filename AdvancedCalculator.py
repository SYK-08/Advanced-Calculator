def Input():
    print("Select operation:\n","1.Addition(+)\n","2.Subtraction(-)\n","3.Multiplication(*)\n","4.Division(/)\n","5.Exponentiation(**)\n","6.Modulo(%)\n","7.Floored quotient or Integer division(//)\n")
    
    op = input("Operation-->")
    num1 = int(input("First Number:"))
    num2 = int(input("Second Number:"))
    answer = str(num1) + op + str(num2)
    print("Answer:")

    if op == "+":
        print(num1 + num2)
    elif op == "-":
        print(num1 - num2)
    elif op == "*":
        print(num1 * num2)
    elif op == "/":
        print(num1 / num2)
    elif op == "**":
        print(num1 ** num2)
    elif op == "%":
        print(num1 % num2)
    elif op == "//":
        print(num1 // num2)
    else:
        print("Invalid Format.")     
Input()

def again():
    while True:
        q1 = input("Do you want to calculate more?(y/n)").lower()
        if q1 == 'n':
            exit()
        elif q1 == 'y':
            Input()
again()
