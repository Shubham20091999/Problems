# n=int(input())
# lst = list(map(int,input().split()))

# sLst = sorted(lst)

# dLst = [0]*n
# for i in range(n):
#     dLst[i] = (lst[i]-sLst[i])

# swapI = None
# swapL = None
# for i in range(n):
#     if(dLst[i] != 0):
#         swapI = i
#         break
# try:
#     swapL = dLst.index(-dLst[swapI])
#     tempLst = lst[:]
#     tempLst[swapI], tempLst[swapL] = tempLst[swapL], tempLst[swapI]
#     if(tempLst == sLst):
#         print('yes')
#         print(f'swap {swapI+1} {swapL+1}')
#         exit(0)
# except ValueError:
#     pass

# revI = -1
# revL = 1

# for i in range(1, n):
#     if(lst[i-1] > lst[i]):
#         if(revL == 1):
#             revI = i-1
#         revL += 1
#     elif(revL != 1):
#         break
# tempLst = lst[:revI]+list(reversed(lst[revI:revI+revL]))+lst[revI+revL:]
# if(sLst == tempLst):
#     print('yes')
#     print(f'reverse {revI+1} {revI+revL}')
#     exit(0)
# print('no')

# ------------------------------
n = int(input())
lst = list(map(int, input().split()))

i = 0
f = n-1


def isSorted(lst: list) -> bool:
    for i in range(1, len(lst)):
        if(lst[i] < lst[i-1]):
            return False
    return True


while lst[i] <= lst[i+1]:
    i += 1
while lst[f-1] <= lst[f]:
    f -= 1

tmplst = lst[:]
tmplst[i], tmplst[f] = tmplst[f], tmplst[i]

if(isSorted(tmplst)):
    print('yes')
    print(f'swap {i+1} {f+1}')
    exit(0)

tmplst = lst[:i]+list(reversed(lst[i:f+1]))+lst[f+1:]
if(isSorted(tmplst)):
    print('yes')
    print(f'reverse {i+1} {f+1}')
    exit(0)
print('no')
