def compare(limit: int) -> int:
    sum_of_sq = sum(i ** 2 for i in range(1, limit + 1))
    sq_of_sum = (limit * (limit + 1) / 2) ** 2

    return int(sq_of_sum - sum_of_sq)

print(compare(100))
