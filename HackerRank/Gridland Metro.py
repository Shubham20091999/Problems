# https://www.hackerrank.com/challenges/gridland-metro/problem
# https://www.geeksforgeeks.org/merging-intervals/

# n, m, k = map(int, input().split())
# # Drictonary of rows and array of start and end positions of the tracks
# pos = {}

# for i in range(k):
#     r, c1, c2 = map(int, input().split())
#     # if current row does not exist in the dict
#     if(r not in pos):
#         pos[r] = [(c1, c2)]
#     else:  # else
#         #
#         posC1 = None
#         posC2 = None
#         rowCheck = pos[r]
#         for j in range(len(rowCheck)):
#             if(posC1 == None):
#                 # if start of the track is at the left of some track
#                 # if start and end is on the same side then break will not happen cuz posC2!=None
#                 if(c1 < rowCheck[j][0]):
#                     posC1 = j
#                 # if start of the track is between some other track
#                 elif(c1 >= rowCheck[j][0] and c1 <= rowCheck[j][1]):
#                     posC1 = j
#             if(posC2 == None):
#                 # if end of the track is between some other track
#                 if(c2 >= rowCheck[j][0] and c2 <= rowCheck[j][1]):
#                     posC2 = j
#                 # if end of the track is after some other track
#                 # if start and end is on the same side then break will not happen cuz posC1!=None
#                 elif(c2 > rowCheck[j][1]):
#                     posC2 = j
#             if(posC1 != None and posC2 != None):
#                 break
#         else:  # if posC1==None or posC2==None
#             # if posC1==None then the current block will be at the start cuz there is something
#             # after the current track but there is nothing before it
#             pos[r].insert(0 if(posC1 == None) else -1, (c1, c2))
#             continue
#         # find the minimum for the start position depending on overlap
#         k1 = min(rowCheck[posC1][0], c1)
#         # find the maximum for the end position depending on overlap
#         k2 = max(rowCheck[posC2][1], c2)
#         # Delete everything between the overlaping positions
#         del pos[r][posC1+1:posC2+1]
#         # insert at the starting position of the overlap
#         pos[r][posC1] = (k1, k2)

# # Number of pos if there were no tracks
# count = n*m

# for row in pos.values():
#     for p in row:
#         # Minusing the tracks
#         count -= p[1]-p[0]+1
# print(count)

# ---------------------------------------
# Python3 program to merge overlapping Intervals
# in O(n Log n) time and O(1) extra space
def mergeIntervals(arr):

    # Sorting based on the increasing order of the start intervals
    arr.sort(key=lambda x: x[0])

    # array to hold the merged intervals
    m = []
    # Starting point of the current interval
    starting = arr[0][0]
    # Ending Point of current interval
    ending = arr[0][1]
    for i in range(1, len(arr)):
        a = arr[i]
        if a[0] > ending:
            m.append([starting, ending])
            ending = a[1]
            starting = a[0]
        else:
            if a[1] >= ending:
                ending = a[1]

    # If there is only single element in the arr
    # OR if last interval in arr is not overllaping with someting else 
    if(len(m)==0 or [starting, ending]!=m[-1]):
        m.append([starting, ending])
    return m


n, m, k = map(int, input().split())
pos = {}

for i in range(k):
    r, c1, c2 = map(int, input().split())
    try:
        pos[r]+=[(c1,c2)]
    except:
        pos[r]=[(c1,c2)]

# Count if there were no tracks
count=n*m

for row in pos.values():
    row=mergeIntervals(row)
    for p in row:
        # Minusing the tracks
        count -= p[1]-p[0]+1
print(count)