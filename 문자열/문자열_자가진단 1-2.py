# for문으로 출력
a = input()

for i in range(len(a)):
    print(a[-(i+1)], end="")

#슬라이싱으로 출력
a = input()
print(a[::-1])
