a = "apple orange banana"
b = "   Hello world!   "

c = a.split()

for i in range(len(c)-1, -1, -1):
    if i ==0:
        print(c[i])
    else :
        print(c[i], end=" ")

print(b)
print(b[3:-3])
