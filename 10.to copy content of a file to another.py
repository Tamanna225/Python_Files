# to copy content of a file to another
def filecopy(fi1,fi2):
    f1 = open(fi1,"r")
    f2 = open(fi2,"w")
    line = f1.readline()
    while line != '':
        f2.write(line)
        line = f1.readline()
    f1.close()
    f2.close()
def main():
    filename1 = input("Enter source file name: ")
    filename2 = input("Enter the destination file name: ")
    filecopy(filename1,filename2)
if __name__ == "__main__" :
    main()
input("Press ENTER to exit")    
    
