# # https://www.hackerrank.com/challenges/cut-the-tree/problem

n = int(input())
vals = list(map(int,input().split()))
t = sum(vals)

adjLi = [[] for _ in range(n)]

# Lets consider array is making two way connections
# From Parent to Child and child to parent
# as we dont know which is child and which is parent
for i in range(n-1):
    u,v = map(int,input().split())
    adjLi[u-1].append(v-1)
    adjLi[v-1].append(u-1)

# Finally will give sum of tree including and below the node i
totVal = vals[:]

# These shows the elements with only one child to parent edge
# that is they are at the end of the tree and these are not parent of any other node
# we are using set because multiple child might have same parents
# it is not useful in this line but it will be useful in iteration
waiting = {i for i in range(n) if len(adjLi[i]) == 1}


while(len(waiting)):
    for i in waiting:
        # if (number of possible parents of i)!=0 
        # if while iterating over waiting removes the node and makes adjLi[i]==0 for some other node
        if(len(adjLi[i])!=0):
             # Removing parent to child connection as we just need child to parent connections
            adjLi[adjLi[i][0]].remove(i)
            # adding the value of child tree
            totVal[adjLi[i][0]] += totVal[i]

    # if number of parents of i==0 then we dont have to add it in waiting
    waiting = {adjLi[i][0] for i in waiting if len(adjLi[i])==1 and len(adjLi[adjLi[i][0]]) == 1}
# finally adjLi will become an array with list of 1 or 0 element
# element in the list in ith position lets call it j will show that the parent of i is that j 
# 0 will be when node is at the starting of the tree

# sum of remaining tree=total-sum of cutted tree
# rt=abs(sum of remaining tree-sum of cutted tree)
ans = abs(t- 2*totVal[0])
for i in range(1,n):
    ans=min(ans,abs(t-2*totVal[i]))

print(ans)