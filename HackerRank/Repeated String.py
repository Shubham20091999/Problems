s=input()
n=int(input())

a=0
for c in s:
    if(c=='a'):
        a+=1

a*=n//len(s)

for c in s[:n-n//len(s)*len(s)]:
    if(c=='a'):
        a+=1

print(a)