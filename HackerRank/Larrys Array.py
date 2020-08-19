# https://www.hackerrank.com/challenges/larrys-array/problem

# ABC->BCA we make two inversions
# ABC->CAB we make two inversions
# thus we have to check if the number of inversions needed for sorting
# if its even than 'YES' otherwise 'NO'
for _ in range(int(input())):
    n=int(input())
    lst=list(map(int,input().split()))

    count=0
    for i in range(1,len(lst)):
        for j in range(0,i):
            if(lst[j]>lst[i]):
                # Do not un comment answer will be worng
                # lst.insert(j,lst.pop(i)) #This line will make it insertion sort 
                count+=1
    # print(lst)
    print('YES' if(count%2==0) else 'NO')