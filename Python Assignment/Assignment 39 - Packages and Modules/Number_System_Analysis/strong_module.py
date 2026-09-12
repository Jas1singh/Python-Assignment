def isStrong(n):
    sum = 0
    temp = n
    while temp>0:
        d = temp % 10
        fact = 1 
        for i in range(d):
            fact = fact * i
        sum = sum + fact
        temp = temp//10

    if sum==n:
        return True
    else:
        return False