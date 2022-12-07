#Calculator using if else
print("I am  a calculator")
x = input("What you want to perform Enter the sign from \n(a)+\n(b)-\n(c)*\n(d)/\n")
num1 = eval(input("Enter 1st value:"))
num2 = eval(input("Enter 2st value:"))
if x == "+":
    r1 = num1 + num2
    print("Your result:",r1)
elif x == "-":
    r2 = num1 + num2
    print("Your result:",r2)
elif x == "*":
    r3 = num1 * num2
    print("Your result:",r3)
elif x == "/":
    if num2 == 0:
        print("division by zero is nOt possible")
    else:
        r4 = num1 / num2
        print("Your result:",r4)
else:
    print("you have entered invalid input")
input("Press ENTER to exit")
