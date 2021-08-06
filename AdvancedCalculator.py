q = input("Should I start the program?(y/n)")
if q == 'n':
    print("Oh okay.")
elif q == 'y':
    print("Select operation:\n","1.Addition(+)\n","2.Subtraction(-)\n","3.Multiplication(*)\n","4.Division(/)\n","5.Exponentiation(**)\n","6.Modulo(%)\n","7.Floored quotient or Integer division(//)\n")

def Input():
    op = input("Operation-->")
    num1 = input("First Number:")
    num2 = input("Second Number:")
    answer = num1 + op + num2
    print("Answer:")

    if op == "+":
        print(int(num1) + int(num2))
    elif op == "-":
        print(int(num1) - int(num2))
    elif op == "*":
        print(int(num1) * int(num2))
    elif op == "/":
        print(int(num1) / int(num2))
    elif op == "**":
        print(int(num1) ** int(num2))
    elif op == "%":
        print(int(num1) % int(num2))
    elif op == "//":
        print(int(num1) // int(num2))
    else:
        print("Invalid Format.")     
Input()

while True:
    q2 = input("Do you want to calculate more?(y/n)")
    if q2 == 'n':
        print("Okay, bye bye.")
        break
    elif q2 == 'y':
       Input()
