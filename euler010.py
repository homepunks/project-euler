def eratosthenes_sum(limit: int) -> int:
    prime = [True] * (limit + 1)

    prime[0] = False
    prime[1] = False

    for p in range(2, int(limit ** 0.5) + 1):
        if prime[p]:
            for mult in range(p * p, limit + 1, p):
                prime[mult] = False

    primes = [i for i in range(2, limit + 1) if prime[i]]

    return sum(primes)
    
print(eratosthenes_sum(2_000_000))
