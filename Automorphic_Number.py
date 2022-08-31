n=int(input())
n_of_digits=len(str(n))
square=n**2
last_digit=square%pow(10,n_of_digits)
if last_digit==n:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")