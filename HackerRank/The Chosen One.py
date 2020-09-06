import math 

p=[0]*10000000
s=[0]*10000000
a=[]
n=int(input())
if n==1:
    print(int(input())+1)
    exit(0)
a=list(map(int,input().split(" ")))

# Saving common divisors of all the numbers before certain index
for i in range(n):
    p[i+1]=math.gcd(a[i],p[i])

# Saving common divisors of all the numbers after certain index
for j in range(n,0,-1):
    s[j]=math.gcd(s[j+1],a[j-1])

# Checking if current number has gcd common with all numbers before and after  
for i in range(1,n+1):
    cur=math.gcd(p[i-1],s[i+1])
    if a[i-1]%cur!=0:
        print(cur)
        exit(0)