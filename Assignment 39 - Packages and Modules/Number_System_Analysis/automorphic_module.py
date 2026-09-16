def isAutomorphic(n):
    square = n * n
    count = 0
    temp = n
    while temp>0:
        count = count+1
        temp = temp // 10

    if square%10**count==n:
        return True

    else:
        return False