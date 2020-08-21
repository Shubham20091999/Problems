class Solution:
    def lengthOfLongestSubstring(self,s: str) -> int:
        d={}
        t=0
        ans=0
        for h,c in enumerate(s):
            if(c in d):
                if(d[c]+1>t):
                    t=d[c]+1
                d[c]=h 
            else:
                d[s[h]]=h
            if(ans<h-t+1):
                ans=h-t+1
        return ans

print(lengthOfLongestSubstring(input()))