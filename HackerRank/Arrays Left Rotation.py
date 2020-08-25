# https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=arrays
n,k=map(int,input().split())
l=list(map(int,input().split()))

for i in range(k,k+n):
    print(l[i%n],end=' ')

print("")