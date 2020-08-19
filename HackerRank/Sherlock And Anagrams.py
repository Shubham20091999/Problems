# https://www.hackerrank.com/challenges/sherlock-and-anagrams
# def Combination2(m):
#     if(m<2):
#         return 0
#     return m*(m-1)//2

# for _ in range(int(input())):
#     s=list(input())
#     substringCount = {}

#     li = [0]*26
#     for i in range(0, len(s)):
#         for j in range(i, len(s)):
#             tempS = ''.join(list(sorted(s[i:j+1])))
#             if(tempS in substringCount):
#                 substringCount[tempS] += 1
#             else:
#                 substringCount[tempS] = 1

#     count = 0

#     for v in substringCount.values():
#         count+=Combination2(v)
#     print(count)
# -------------------------

from collections import Counter
class hashableCounter(Counter):
    def __hash__(self):
        return hash(tuple(sorted(self.items())))

def Combination2(m):
    if(m<2):
        return 0
    return m*(m-1)//2

for _ in range(int(input())):
    s=list(input())
    substringCount = {}

    li = [0]*26
    for i in range(0, len(s)):
        for j in range(i, len(s)):
            tempS = hashableCounter(s[i:j+1])
            if(tempS in substringCount):
                substringCount[tempS] += 1
            else:
                substringCount[tempS] = 1

    count = 0

    for v in substringCount.values():
        count+=Combination2(v)
    print(count)