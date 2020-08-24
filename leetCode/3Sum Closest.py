# https://leetcode.com/problems/3sum-closest/
class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        m=float('inf')
        ans=0
        for i,n in enumerate(nums):
            l=i+1
            r=len(nums)-1
            while l<r:
                diff=n+nums[l]+nums[r]-target
                if(abs(diff)<m):
                    m=abs(diff)
                    ans=diff+target
                if(diff<0):
                    while nums[l]==nums[l+1] and l+1<r:
                        l+=1
                    l+=1
                elif(diff>0):
                    while nums[r]==nums[r-1] and r-1>l:
                        r-=1
                    r-=1
                else:
                    return target
        return ans