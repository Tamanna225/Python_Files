# To store and display student info using admission number
SCL = dict()
i = 1
flag = 0
n= int(input("Enter number of enteries:"))
while i <=n:
    Adm = input("\nEnter admission number of a student:")
    nm = input("Enter name of the student:")
    sec = input("Enter class and section:")
    per = float(input("Enter percentage of the student:"))
    b = (nm,sec,per)
    SCL[Adm] = b
    i = i + 1
l = SCL.keys()

for i in l:
    print("\nAdmno-",i,":")
    z = SCL[i]
    print("Name\t","class\t","per\t")
    for j in z:
        print(j,end = "\t")
input("\nPress ENTER to exit")        
          
