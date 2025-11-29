def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
        
    return True


target = 600_851_475_143
x = 2

while True:
    if is_prime(target):
        print(int(target))
        exit()

    if target % x == 0:
        target /= x

    x += 1
