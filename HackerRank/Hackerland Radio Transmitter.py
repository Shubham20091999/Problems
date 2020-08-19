# https://www.hackerrank.com/challenges/hackerland-radio-transmitters/problem

# Partial Solution 4/31 Failed
# n, k = map(int, input().split())
# l = sorted(list(map(int, input().split())))

# minNumLighted = l[0]
# ans = 0
# lightAt = l[0]

# for i in range(1, len(l)):
#     if(l[i]-minNumLighted > k):
#         if(minNumLighted == lightAt):
#             lightAt = l[i-1]
#             ans += 1
#         if(minNumLighted != lightAt):
#             if(l[i]-lightAt > k):
#                 minNumLighted = l[i]
#                 lightAt = l[i]

# print(ans+int(l[-1]-lightAt>k))

# --------------------
n,k = map(int, input().split())
l = sorted(list(map(int, input().split())))

# what does this mean that place transmitter in a such way that it will handle houses on left and right sides comfortably
# So first you are at left most position.. iterate over and find middle position where (middle-left==k) and then find right most position where (right-middle<=k)

count_trans = 0
last = l[0]
i = 0
while(i < n):
    count_trans = count_trans + 1
    next_point = l[i] + k
    while(i < n and l[i] <= next_point):
        i = i + 1
    next_point = l[i-1] + k
    while(i < n and l[i] <= next_point):
        i = i + 1

print(count_trans)