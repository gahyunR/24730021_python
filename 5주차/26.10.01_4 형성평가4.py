#sum()을 사용하는 방법
N = int(input())
lst = []

for i in range(N):
    temp = int(input())
    lst.append(temp)

print(int(sum(lst)/N))


#total

N =int(input())
lst = []

for i in range(N):
    temp = int(input())
    lst.append(temp)

total = 0

for i in lst:
    total += i

print(int(total / N))
