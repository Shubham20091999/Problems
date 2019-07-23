n,k=map(int,input().split())

sr=[1]*k
sr.append(k)
for i in range(k+1,n):
    sr.append(0)
    sr[i]=2*sr[i-1]-sr[i-k-1]
print(sr[n-1]%1000000007)

#Bad Method
# n,k=map(int,input().split())

# def kFibo(n,k):
#     if(n<=k):
#         return 1
#     ans=0
#     for i in range(0,k):
#         ans+=kFibo(n-i-1,k)
#     return ans

# print(kFibo(n,k))
