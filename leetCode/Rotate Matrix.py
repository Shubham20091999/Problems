class Solution:
    def rotate(self, m: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(m)
        for i in range(n//2):
            for j in range(i,n-i-1):
                m[i][j],m[j][n-1-i],m[n-1-i][n-1-j],m[n-1-j][i]=m[n-1-j][i],m[i][j],m[j][n-1-i],m[n-1-i][n-1-j]

class Solution:
    def rotate(self, m: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(m)
        for i in range(0,n-1):
            for j in range(i+1,n):
                m[i][j],m[j][i]=m[j][i],m[i][j]
            m[i].reverse()
        m[-1].reverse()
            