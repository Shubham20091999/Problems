
def jumpingOnClouds(c):
    ans=0
    i=0
    while True:
        for j in range(2,0,-1):
            if(i+j>=len(c)):
                ans+=1
                return ans
            elif(c[i+j]==1):
                continue
            elif(c[i+j]==0):
                i=i+j
                ans+=1
                if(i==len(c)-1):
                    return ans
                break


# c="00100001000010000010100010010001010000000010010100"
# c="000010"
c="0010010"
print(jumpingOnClouds(c))