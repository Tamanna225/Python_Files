# To insert a record in student file
import pickle
record = []
while True:
    roll_no = int(input("Enter student roll no: "))
    name = input("Enter the student name: ")
    marks = int(input("Enter the marks obtained: "))
    data = [roll_no, name, marks]
    record.append(data)
    choice = input("Wish to enter new record (Y/N)? ")
    if choice.upper() == "N":
        break
f = open("student","wb")
pickle.dump(record, f)
print("Record Added")
f.close()
input("Press ENTER to exit")
