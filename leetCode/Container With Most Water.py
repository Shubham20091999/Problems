# https://leetcode.com/problems/container-with-most-water
class Solution:
    def maxArea(self, height: list[int]) -> int:
        t = 0
        h = len(height)-1
        m = 0
        while t < h:
            m = max(m, min(height[h], height[t])*(h-t))
            if(height[t] < height[h]):
                t += 1
            else:
                h -= 1
        return m
