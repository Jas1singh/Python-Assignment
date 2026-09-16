def isArmstrong(n):
    count = 0
    temp = n
    while temp>0:
        count = count+1
        temp = temp // 10

    sum = 0
    t = n
    while t>0:
        d = t % 10 
        sum = sum + d**count  
        t = t//10

    if sum==n:
        return True
    else:
        return False