# fibonacci series using recursion
def fibo(n):
    if n<= 1:
        return n
    else:
        return(fibo(n-1)+fibo(n-2))
nterms = int(input("how many terms required in series: "))
print("Fibonacci sequence generated is: ")
for i in range(nterms):
    print(fibo(i))
input("Press ENTER to exit")
