# https://www.hackerrank.com/challenges/magic-square-forming/problem


def formingMagicSquare(s):
    squares = [
        [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
        [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
        [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
        [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
        [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
        [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
        [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
        [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
    ]
    minV=float('inf')
    for square in squares:
        tempV=0
        for m in range(len(square)):
            for n in range(len(square[0])):
               tempV+=abs(square[m][n]-s[m][n])
        if(minV>tempV):
            minV=tempV
    return minV 


