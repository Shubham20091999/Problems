#using Dictionary
def minimumSwaps(arr):
    ans=0
    dict={}
    l=list(range(1,len(arr)+1))
    for i in range(0,len(arr)):
         if(arr[i]!=l[i]):
            if(l[arr[i]-1]==arr[i]):
                (l[arr[i]-1],l[i])=(l[i],l[arr[i]-1])
                dict[l[i]]=i
                dict[l[arr[i]-1]]=arr[i]-1
                ans+=1
                continue
            else:
                j=dict[arr[i]]
                (l[j],l[i])=(l[i],l[j])
                (dict[l[i]],dict[l[j]])=(i,j)
                ans+=1
    return ans   

#using list
def minimumSwaps1(arr):
    ans=0
    l=list(range(1,len(arr)+1))
    listofPos=list(range(0,len(arr)))
    for i in range(0,len(arr)):
         if(arr[i]!=l[i]):
            j=listofPos[arr[i]-1]
            (l[j],l[i])=(l[i],l[j])
            (listofPos[l[i]-1],listofPos[l[j]-1])=(i,j)
            ans+=1
    return ans     


# arr=[7, 1, 3, 2, 4, 5, 6]
# print(minimumSwaps2(arr))

# n = int(input())

# arr = list(map(int, input().rstrip().split()))

# res = minimumSwaps(arr)

# print(res)


f= open("Input2.txt","r")
contents =list(map(int,(f.read().split())[1:]))
print(minimumSwaps1(contents))
