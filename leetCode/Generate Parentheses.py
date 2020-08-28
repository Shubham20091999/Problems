# class Solution:
#     def generateParenthesis(self, n: int) -> list:
#         if(n==0):
#             return []
#         ans=set()
#         ans.add(tuple(['(',')']))
#         temp=set()
#         for _ in range(1,n):
#             for bracs in ans:
#                 bracs=list(bracs)
#                 for i in range(len(bracs)):
#                     temp.add(tuple(bracs[:i]+['(',')']+bracs[i:]))
#             ans,temp=temp,ans
#             temp.clear()
#         for a in ans:
#             yield (''.join(a))

# Backtracking


# class Solution1:
#     def generateParenthesis(self, N):
#         ans = []

#         def backtrack(S='', left=0, right=0):
#             if len(S) == 2 * N:
#                 ans.append(S)
#                 return
#             # if number of left brackets<N
#             if left < N:
#                 backtrack(S+'(', left+1, right)
#             # if number of right brackets<left
#             if right < left:
#                 backtrack(S+')', left, right+1)

#         backtrack()
#         return ans

from collections import defaultdict
memo = defaultdict(lambda: None)
class Solution:
    def generateParenthesis(self, N):
        if N == 0:
            return ['']
        ans = []
        if(memo[N] != None):
            return memo[N]
        for c in range(N):
            # getting all possible solutions of size n-1

            # if c==0
            # then N-1-c==N-1
            for left in self.generateParenthesis(c):
                for right in self.generateParenthesis(N-1-c):
                    ans.append('({}){}'.format(left, right))

        return ans