n=int(input())
sum=0
sqr=n*n
while sqr>0:
    sum=sum+sqr%10
    sqr=sqr//10
if n==sum:
    print("Neon Number")
else:
    print("Not Neon Number")