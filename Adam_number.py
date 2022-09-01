def reversedigits(n):
    rev=0
    while n>0:
        rev=rev*10+n%10
        n=n//10
    return rev
def sqr(n):
    return (n*n)
def checkAdam(n):
    a=sqr(n)
    b=sqr(reversedigits(n))
    if(a==reversedigits(b)):
        return True
    else:
        return False
n=int(input())
if checkAdam(n):
    print("True")
else:
    print("False")