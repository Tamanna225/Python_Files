#Calculator using function
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
def calc(a,b):
    add = a+b
    sub = a-b
    mul = a*b
    div = a/b
    return add,sub,mul,div
result = calc(a,b)
print("The results obtained are : ")
for i in result:
    print(i)
