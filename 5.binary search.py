#To perform Binary search
from random import randint
def binsearch(lst,item):
    m = len(lst)//2
    l = 0
    h = len(lst) - 1
    while lst[m] != item and l<=h:
        if item > lst[m]:
            l = m+1
        else:
            h = m - 1
        m = (l+h)//2
    if l > h:
        return None
    else:
        return m
a = []
for i in range(10):
    a.append(randint(1,20))
a.sort()
print(a)

value = int(input("Enter element to search: "))
print("Element found at the index : ", binsearch(a,value))
input("Press ENTER to exit")
