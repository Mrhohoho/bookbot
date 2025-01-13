print("hello world")

def main():
    with open("books/frankenstein.txt") as f:

        file=f.read()
        #print(file)

        print(words(file))

        print(eachchar(file))
        print(getsome(eachchar(file)))
        pass

def getsome(indic):
    tempstr=""

    for (k,v) in indic.items():

        tempstr=tempstr+"\n"+str(k)+" = "+str(v)

    return tempstr
    pass

def words(intxt:str)->int:

    #temp = file.split(" ")
    temp = intxt.split()
    return len(temp)
    pass

def eachchar(intxt:str):

    tempt=intxt.lower()
    tdic={}
    for i in range(97,122+1):
        tdic[chr(i)]=0
    
    for i in intxt:
        if i in tdic:
            tdic[i]=tdic[i]+1
            pass
    

    return tdic
    pass


main()