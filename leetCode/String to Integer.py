# https://leetcode.com/problems/string-to-integer-atoi/

class Solution:
    def myAtoi(self, st: str) -> int:
        ans=0
        digitCaught=False
        m=None
        p=0
        for s in st:
            if(s==' '):
                if(not(digitCaught) and m==None):
                    continue
                else:
                    break
            elif(s=='-'):
                if(not(digitCaught) and m==None):
                    m=False
                else:
                    break
            elif(s=='+'):
                if(not(digitCaught) and m==None):
                    m=True
                else:
                    break
            elif(s.isdigit()):
                digitCaught=True
                ans=ans*10+int(s)
            else:
                break
                
        ans*=-1 if(m==False) else 1
        if(ans>2**31-1):
            return 2**31-1
        if(ans<-2**31):
            return -2**31
        return ans
                