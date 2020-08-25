from collections import Counter
counter=Counter()
counterOCounter=Counter()
for _ in range(int(input())):
    l,r=map(int,input().split())
    if(l==1):
        if(counterOCounter[counter[r]]>0):
            counterOCounter[counter[r]]-=1
        counter[r]+=1
        counterOCounter[counter[r]]+=1
    elif(l==2):
        # Delete one occurence if present
        if(counter[r]>0):
            counterOCounter[counter[r]]-=1
            counter[r]-=1
            counterOCounter[counter[r]]+=1
    else:
        if(counterOCounter[r]>0):
            print(1)
        else:
            print(0)
