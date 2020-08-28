# BackTracking
class Solution:
    def combinationSum(self, c: list, t: int):
        ans = []
        c.sort()

        def dfs(s, lst, i):
            if(s == t):
                ans.append(tuple(lst))
                return
            for j in range(i, len(c)):
                if(s+c[j] > t):
                    break
                lst.append(c[j])
                dfs(s+c[j], lst[:], j)
                lst.pop(-1)

        for i in range(len(c)):
            if(c[i] > t):
                break
            dfs(c[i], [c[i]], i)
        return ans

    def combinationSum2(self, c: list, t: int):
        ans = []
        c.sort()
        def dfs(s, lst, i):
            if(s == t):
                ans.append(tuple(lst))
                return
            for j in range(i+1, len(c)):
                if(s+c[j] > t):
                    break
                if(c[j]==c[j-1] and j!=i+1):
                    continue

                lst.append(c[j])
                dfs(s+c[j], lst[:], j)
                lst.pop(-1)
        dfs(c[0], [c[0]], 0)
        for i in range(1, len(c)):
            if(c[i] > t):
                break
            if(c[i] == c[i-1]):
                continue
            dfs(c[i], [c[i]], i)
        return ans

print(Solution().combinationSum2([2, 5, 5, 2, 1, 2], 5))
