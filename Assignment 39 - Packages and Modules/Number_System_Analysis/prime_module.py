def isPrime(n):
    if n==0 or n==1:
        return False

    if n>1:
        for i in range(2,n//2+1):
            if n%i==0:
                return False
            else:
                return True