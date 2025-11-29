ceiling = 999
check = 0


for x in range(ceiling, 0, -1):
    for y in range(ceiling, 0, -1):
        num = x * y
        if int(str(num)[::-1]) == num and num > check:
            check = num

print(check)
