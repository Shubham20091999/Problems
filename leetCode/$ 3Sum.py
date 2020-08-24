# https://leetcode.com/problems/3sum/
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        ans=[]
        nums.sort()
        for i,num in enumerate(nums):
            if(i>0 and num==nums[i-1]):
                continue
            l=i+1
            r=len(nums)-1
            while l<r:
                s=num+nums[l]+nums[r]
                if(s>0):
                    r-=1
                elif(s<0):
                    l+=1
                else:
                    ans.append((num,nums[l],nums[r]))
                    if(nums[l]==nums[r]):
                        break
                    while nums[l]==nums[l+1]:
                        l+=1
                    while nums[r]==nums[r-1]:
                        r-=1
                    r-=1
                    l+=1
        return ans