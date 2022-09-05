sum=0
n=int(input())
temp=n
while n:
    i=1
    fact=1
    rem=n%10
    while i<=rem:
        fact=fact*i
        i=i+1
    sum=sum+fact
    n=n//10
if sum==temp:
    print("The number %d is a strong number"%temp)
else:
    print("The number %d is not a strong number"%temp)