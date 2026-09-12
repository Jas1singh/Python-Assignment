def isSpy(n):
    sum = 0
    prod = 1
    temp = n
    while temp>0:
        d = temp % 10
        sum = sum + d
        prod = prod * d
        temp = temp // 10

    if sum == prod:
        return True
    
    else:
        return False