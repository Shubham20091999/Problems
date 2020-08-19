# https://www.nayuki.io/page/next-lexicographical-permutation-algorithm
# https://www.hackerrank.com/challenges/bigger-is-greater/problem

n = int(input())
for _ in range(n):
    arr = list(input())
    # Find non-increasing suffix
    i = len(arr) - 1
    while i > 0 and arr[i - 1] >= arr[i]:
        i -= 1  
    if i <= 0:
        print('no answer')
        continue
    # Find successor to pivot
    j = len(arr) - 1
    while arr[j] <= arr[i - 1]:
        j -= 1  
    arr[i - 1], arr[j] = arr[j], arr[i - 1]
	
	# Reverse suffix
    arr[i : ] = arr[len(arr) - 1 : i - 1 : -1]
    print(''.join(arr))
