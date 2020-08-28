# # Good Enough O(m+n) solution
# class Solution:
#     def findMedianSortedArrays(self, nums1: list, nums2: list) -> float:
#         n = len(nums1)
#         m = len(nums2)
#         finalPos = (m+n)//2+1
#         i = 0
#         i1 = 0
#         i2 = 0
#         v = -1
#         prev = -1
#         while i != finalPos:
#             prev = v
#             if(i1 != len(nums1) and (i2 == len(nums2) or nums1[i1] < nums2[i2])):
#                 v = nums1[i1]
#                 i1 += 1
#             else:
#                 v = nums2[i2]
#                 i2 += 1
#             i += 1

#         if((m+n) % 2 == 0):
#             return (v+prev)/2
#         else:
#             return v

# https://www.youtube.com/watch?v=LPFhl65R7ww

class Solution:
    def findMedianSortedArrays(self, A, B):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # n>=m 
        m, n = len(A),len(B)
        if n<m:
            A, B, m, n = B, A, n, m
        
        # 
        imin, imax, halfLen = 0, m, (m+n+1)/2
        while(imin <= imax):
            i = int((imin+imax)/2)
            j = int(halfLen)-i
            if i > 0 and A[i-1] > B[j]:
                imax = i - 1
            elif i < m and A[i] < B[j-1]:
                imin = i + 1
            else:
                # i is perfect
                if i==0:
                    maxLeft = B[j-1]
                elif j==0:
                    maxLeft = A[i-1]
                else:
                    maxLeft = max(A[i-1], B[j-1])
                
                if (m+n) % 2 == 1:
                    return maxLeft
                else:
                    if i==m:
                        minRight = B[j]
                    elif j==n:
                        minRight = A[i]
                    else:
                        minRight = min(B[j],A[i])
                return (maxLeft+minRight)/2

print(Solution().findMedianSortedArrays([1, 2], [3, 4]))
