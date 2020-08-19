# https://www.hackerrank.com/challenges/journey-to-the-moon/problem

# import sys 
# sys.setrecursionlimit(10**6) 

n, p = map(int, input().split())

lst = [[] for _ in range(n)]

# Connections from parent to child and child to parent
for i in range(p):
    l, r = map(int, input().split())
    lst[l].append(r)
    lst[r].append(l)

# Recursive Count Size of tree
# Segmentation fault because the depth of the recursion tree is exceeded
def countTree(node, skipNode=None):
    ret = 1
    for child in lst[node]:
        if(child != skipNode):
            ret += countTree(child, node)
    lst[node] = []
    return ret

# Iterative Count the size of tree
def countTree1(node):
    # set of all the nodes which are counted for
    # Bcuz there might be repeated pairing with different parts of tree
    # eg
    # 2-10
    # 10-3
    # 2-3 
    closed=set()
    
    # nodes we have to account for in next iteration 
    openNodes=[node]

    # While size of openNodes!=0
    while(len(openNodes)):
        # remove the first node
        p=openNodes.pop(0)
        # add it to the closed list
        closed.add(p)
        for child in lst[p]:
            # if child is not in closed
            # Bcuz child contains connection to parent so we dont want to include it again
            # Or there might be some repeated connections as explained while explaining closed
            if(child not in closed):
                openNodes.append(child) 
        # making the list size zero for all the nodes so that we dont need to iterate over them in the main loop (0,n)
        lst[p]=[]
    
    return len(closed)


named = []

for i in range(n):
    if(len(lst[i]) == 0):
        continue
    else:
        named.append(countTree1(i))
nameLess = n-sum(named)

# if both form nameless country
count=nameLess*(nameLess-1)//2

# if one from named country
accountedFor=n
for i in named:
    count+=i*(accountedFor-i)
    # So that we dont repeat the pairs
    accountedFor-=i
print(count)
