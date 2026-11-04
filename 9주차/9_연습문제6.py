max_num = 0

while True:
    num = int(input())

    if num == 0:
        break

    if num > max_num:
        max_num = num


print(max_num)
