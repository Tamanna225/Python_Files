# Bubble sort
def bsort():
    l = [12,79,34,99,78,50]
    n = len(l)
    print("original list: ",l)
    for i in range(n-1):
        for j in range(n-i-1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
    print("List after sorting is: ",l)
bsort()    
