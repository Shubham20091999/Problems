# https://www.hackerrank.com/challenges/non-divisible-subset/problem

n, k = map(int, input().split())
numbers = map(int, input().split())

counts = [0] * k
# Conting the numbers with same mod wrt k 
for number in numbers:
    counts[number % k] += 1

# So that we add atleast one of the number which is divisible by k
# as we are cheacking the sum of only 2 elements
count = min(counts[0], 1)

# Considering k as odd number
for i in range(1, k//2+1):
    # There can be only one number modulo whose sum is divisible by k
    # eg num=5 and k=3 the numbers whose mod is 2 cannot be a part of the same set
    if i != k - i:
        count += max(counts[i], counts[k-i])
# if k is even then we will have one number whose pair doesnot exist
# if k=4, pair of 2 doesnot exist
if k % 2 == 0:
    count += min(1,count[k/2])

print(count)
