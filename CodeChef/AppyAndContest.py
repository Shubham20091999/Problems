import math

n,a,b,k=(11,9,3,8)  
ans=0
gcd=math.gcd(a,b)
lcm = (a*b)/gcd
ans+= n//a
ans+= n//b 
ans-= 2*(n//lcm)
print(ans)
if(ans>=k):
    print("Win")
else:
    print("Lose")
