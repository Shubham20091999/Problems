
# Complete the countingValleys function below.
def countingValleys(n, s):
    temp=0
    pre_temp=0
    ans=0
    for i in range(n):
        if(s[i]=='U'):
            temp+=1
        else:
            temp-=1
        if(pre_temp<0 and temp>=0):
            ans+=1
        pre_temp=temp
    return ans


n = 8

s = "UDDDUDUU"

print(countingValleys(n,s))