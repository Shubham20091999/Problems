def highestValuePalindrome(num, n, k):
    changesAt = set()
    # Making Palindrom
    for i in range(0, n//2):
        if(num[i] != num[n-i-1]):
            if(k == 0):
                return '-1'
            k -= 1
            changesAt.add(i)
            num[i] = max(num[i], num[n-i-1])
            num[n-i-1] = max(num[i], num[n-i-1])
    #Maximizing palindrome
    for i in range(0,n//2):
        if(num[i]!='9'):
            if(i in changesAt and k-1>=0):
                num[i]='9'
                num[n-i-1]='9'
                k-=1
            elif(k-2>=0):
                num[i]='9'
                num[n-i-1]='9'
                k-=2
    if(k>0):
        if(n%2==1):
            num[n//2]='9'
            k-=1

    return ''.join(num)
    


n, k = map(int,input().split())
num = list(input())
print(highestValuePalindrome(num, n, k))
