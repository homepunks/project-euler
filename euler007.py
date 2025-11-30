def gen_nth_prime(n: int) -> int:
    if n == 0:
        raise ValueError("Index must be a natural number greater than 0.")
    if n == 1:
        return 2

    primes = [2]
    candidate = 3

    while (len(primes) <= n):
        is_prime = True
        for i in primes:
            if i * i > candidate:
                break
            if candidate % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(candidate)
        candidate += 2

    return primes[n - 1]

print(gen_nth_prime(10001))
        
