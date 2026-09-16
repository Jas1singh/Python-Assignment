def digitSum(n):
    sum = 0
    while n > 0:
        d = n % 10
        sum = sum + d
        n = n // 10

    return sum