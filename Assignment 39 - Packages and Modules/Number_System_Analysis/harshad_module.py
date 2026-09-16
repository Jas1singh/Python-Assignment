def isHarshad(n):
    sum = 0
    temp = n
    while temp>0:
        d = temp % 10
        sum = sum + d
        temp = temp // 10

    if n%sum==0:
        return True

    else:
        return False
