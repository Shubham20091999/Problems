


def repeatedString0(s, n):
    m=len(s)
    ans=0
    for i in range(0,n):
        if(s[i%m]=='a'):
            ans+=1
    return ans

def repeatedString(s,n):
    num=n//len(s)
    extra=n%len(s)
    ans=0
    for i in range(0,len(s)):
        if(s[i]=='a'):
            ans+=1
    ans*=num
    for i in range(0,extra):
        if(s[i]=='a'):
            ans+=1
    return ans

s="aba"
n=10

print(repeatedString(s,n))