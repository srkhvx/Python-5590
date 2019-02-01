
def Question1a():
    start=100
    stop=500
    for i in range (start,stop):
        p=str(i)
        if(int(p[0])%2!=0):
            if(int(p[1])%2!=0):
                if(int(p[2])%2!=0):
                    print(int(p))

def Question1b():
    start=100
    stop=5000
    for i in range (start,stop):
        p=str(i)
        temp=True
        for j in range(len(p)):
            if(int(p[j])%2==0):
                temp=False
                break
        if(temp):
            print(int(p))

def Question2():
    list1=["1", "4", "0", "6", "9"]
    temp=[]
    final=[]
    for i in list1:
        temp.append(int(i))
    temp.sort()
    for i in temp:
        final.append(str(i))
    print(final)

def Question3():
    fileName = input("ENTER FILE NAME")
    infile = open(fileName, 'r')
    line = infile.readline()
    while line != "":
        letters = 0
        words = 1
        previous = ""
        for i in line:
            if i.isalpha():
                letters += 1
            elif i == " ":
                if previous != i:
                    words += 1
            previous = i
        print(line, " ---> ", " Words = ", words, " , Letters = ", letters)
        line = infile.readline()

if __name__ == '__main__':
    Question3()