# https://www.hackerrank.com/challenges/lilys-homework/problem
n=int(input())
l=list(map(int,input().split()))


def solution(l,sortedL):
    lookUp=dict()
    # Dictionary with key as num and value as position
    for i in range(n):
        lookUp[l[i]]=i

    swaps=0
    # Swaping to each element of list to its actual position and updating the dictionary
    for i in range(len(l)):
        if(l[i]!=sortedL[i]):
            swaps+=1
            newi=lookUp[sortedL[i]]
            lookUp[l[i]]=newi
            l[i],l[newi]=l[newi], l[i]
    return swaps

sortedL=sorted(l)
# minimum will be when the list is sorted or reverse sorted
# Making a copy in first function call so that we dont use sorted list for next function call
print(min(solution(l[:],list(sortedL)),solution(l,list(reversed(sortedL)))))