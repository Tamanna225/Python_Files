# to store and display multiple integers in and from a binary file
def binfile():
    import pickle
    file = open("data.txt","wb")
    while True:
        x = int(input("Enter the integer: "))
        pickle.dump(x,file)
        ans = input("do you want to enter more data: ")
        if ans.upper()=="N":
            break
    file.close()
    file = open("data.txt","rb")
    try:
        while True :
            y = pickle.load(file)
            print(y)
    except EOFError :
        pass
    file.close()
        
binfile()        
    
input("Press ENTER to exit")
