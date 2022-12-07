# Insertion sort
a = [70,23,99,67,84,78,101]
print("Original list : ", a)
for i in a:
    j = a.index(i)
    while j > 0:
        if a[j-1] > a[j]:
            a[j-1], a[j] = a[j], a[j-1]
        else:
            break
        j = j-1
print("List after sorting: ", a)
input("\n Press ENTER to exit")
