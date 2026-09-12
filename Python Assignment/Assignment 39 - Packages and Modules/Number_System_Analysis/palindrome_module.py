def isPalindrome(n):
    temp = n
    rev = 0
    while temp>0:
        d = temp % 10
        rev = rev * 10 + d
        temp = temp//10

    if rev==n:
        return True
    else:
        return False