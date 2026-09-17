def printPattern(rows=6, cols=5, char="A"):
    for _ in range(rows):
        for _ in range(cols): 
            print(char, end=" ")
        print()

printPattern(3,10, "*")
printPattern(3)
