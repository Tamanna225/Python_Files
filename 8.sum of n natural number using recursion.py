#sum of n natural number using recursion
def rsum(n):
    if n<= 1:
        return n
    else:
        return n + rsum(n-1)
x = int(input("Enter a number: "))
if x<0:
    print("Enter a positive number: ")
    rsum()
else:
    print("The sum is: ",rsum(x))
input("Press ENTER to exit")    
