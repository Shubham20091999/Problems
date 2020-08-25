# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if(len(digits)==0):
            return []
        d=['abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        ans=list(d[int(digits[0])-2])
        temp=[]
        for num in digits[1:]:
            for p in ans:
                for q in d[int(num)-2]:
                    temp.append(p+q)
            # So that do not create new array every time
            ans,temp=temp,ans
            temp.clear()
        return ans
            