Input = input("Enter the file you want to read  ")
def CountWord(data):
    content = open(data)
    content2 = content.read()
    print(content2)
    words = content2.split()
    Nowords = 1
    Nowords = Nowords + len(words)
    print(Nowords)
    charN = 0
    for i in content2:
        charN = charN+1
    print(charN)    




CountWord(Input)
