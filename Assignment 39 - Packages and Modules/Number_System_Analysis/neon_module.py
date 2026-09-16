def isNeon(n):
    square = n * n
    sum = 0
    temp = square
    while temp>0:
        d = temp % 10
        sum = sum + d
        temp = temp // 10

    if sum == n:
        return True

    else:
        return False