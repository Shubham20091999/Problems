# https://leetcode.com/problems/zigzag-conversion/
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if(numRows==1):
            return s
        nxt=0
        ans=''
        while nxt<len(s):
            ans+=s[nxt]
            nxt+=(numRows-1)*2
        
        for i in range(1,numRows-1):
            p=0
            nxt=i
            while nxt<len(s):
                ans+=s[nxt]
                p+=1
                nxt=(p//2*2+1)*i+(p+1)//2*(numRows-1-i)*2
                
        nxt=numRows-1
        while nxt<len(s):
            ans+=s[nxt]
            nxt+=(numRows-1)*2
        
        return ans