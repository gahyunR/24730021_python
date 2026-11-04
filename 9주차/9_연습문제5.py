num = int(input())
total = 1

for i in range(1, num + 1):
    total *= i

    if total >= num:
        print(i)
        break
