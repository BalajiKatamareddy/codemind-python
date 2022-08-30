n=int(input())
sum=0
product=1
m=n
while m>0:
    d=m%10
    sum=sum+d
    product=product*d
    m=m//10
if sum==product:
    print("Spy Number")
else:
    print("Not Spy Number")