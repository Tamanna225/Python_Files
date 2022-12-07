# Factorial using recursion
def rfact(n):
    if n == 1:
        return n
    else:
        return n*rfact(n-1)
x = int(input("Enter a number: "))
if x<0:
    print("Factorial of negative number doesn't exists")
elif x == 0:
    print("Factorial of 0 is 1")
else:
    print("The Factorial of",x,"is",rfact(x))
input("Press ENTER to exit")    
