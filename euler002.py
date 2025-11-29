fib = [0, 1]

total = sum(fib)
while fib[1] < 4_000_000:
    fib[0], fib[1] = fib[1], fib[0] + fib[1]
    if fib[1] % 2 == 0:
        total += fib[1]

print(total)
