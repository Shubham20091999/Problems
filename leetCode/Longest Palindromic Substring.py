class Solution:
    def longestPalindrome(self, s: str) -> str:
        if(len(s) == 0):
            return ''
        ans = s[0]
        for i in range(1, len(s)):
            temp = ''
            j = 0
            for j in range(0, min(i, len(s)-i)):
                if(s[i-j-1] == s[i+j]):
                    temp = s[i-j-1:i+j+1]
                else:
                    break
            k1=s[i-j-1:i+j+2]
            k2=s[i+j+1:i-j-2 if(i-j-2>0) else None:-1]
            if(k1==k2):
                temp=s[i-j-1:i+j+2]
                for k in range(j, min(i, len(s)-i-1)):
                    if(s[i-k-1] == s[i+k+1]):
                        temp = s[i-k-1:i+k+2]
                    else:
                        break
            else:
                if(len(temp)>len(ans)):
                    ans = temp
        return ans

# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         if(len(s)==0):
#             return ''
#         ans = s[0]
#         for i in range(1, len(s)):
#             tempEven=''
#             for j in range(0,min(i,len(s)-i)):
#                 if(s[i-j-1]==s[i+j]):
#                     tempEven=s[i-j-1]+tempEven+s[i+j]
#                 else:
#                     break
#             tempOdd=s[i]
#             for j in range(0,min(i,len(s)-i-1)):
#                 if(s[i-j-1]==s[i+j+1]):
#                     tempOdd=s[i-j-1]+tempOdd+s[i+j+1]
#                 else:
#                     break
#             if(len(tempEven)>len(ans)):
#                 ans=tempEven
#             if(len(tempOdd)>len(ans)):
#                 ans=tempOdd
#         return ans

print(Solution().longestPalindrome(input()))
