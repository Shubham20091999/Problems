# l = sorted(list(map(int, input().split())))

# # tot=0
# # for x in range(1,l[0]+1):
# #     for y in range(x,l[1]+1):
# #         for z in range(y,l[2]+1):
# #             for w in range(z,l[3]+1):
# #                 tot+=1
# # print(tot)

# tot = 0
# for x in range(1, l[0]+1):
#     for z in range(x, l[2]+1):
#         tot += (min(z, l[1])-x+1)*(l[3]-z+1)


# def getCounter(m, n):
#     counter = [[]]*4096
#     for i in range(1, m+1):
#         for j in range(i, n+1):
#             try:
#                 counter[i ^ j] += [(i, j)]
#             except:
#                 counter[i ^ j] = [(i, j)]
#     return counter


# g1 = getCounter(l[0], l[3])
# g2 = getCounter(l[1], l[2])

# zeros = 0
# completed = set()  # take Care
# for k in range(4095):
#     for m in g1[k]:
#         try:
#             for n in g2[k]:
#                 l = tuple(sorted([m[0], n[0], n[1], m[1]]))
#                 if(l not in completed):
#                     completed.add(l)
#                     zeros += 1
#         except:
#             pass


# # zeros=0
# # completed=set()
# # for i in range(1,l[1]+1):
# #     for j in range(i,l[2]+1):
# #         try:
# #             for k in g1[i^j]:
# #                 l=tuple(sorted([i,j,k[0],k[1]]))
# #                 if(l not in completed):
# #                     completed.add(l)
# #                     zeros+=1
# #         except:
# #             pass

# print(tot-zeros)

def beautifulQuadruples(a, b, c, d):
    a,b,c,d = sorted([a,b,c,d])
    # Maximum num that c^d will take
    max_num = 2 ** (len(bin(d))-2)

    # To save the count of c^d
    cnt = [0] * max_num

    # total number of c^d
    all_cnt = 0
    for i in range(1,c+1):
        for j in range(i,d+1):
            cnt[i^j] += 1
            all_cnt+=1
    ret = 0
    # Cuz b is bigger than a
    for i in range(1,b+1):
        for j in range(1,min(a+1,i+1)):
            # Removing all the possible pairs where i^j is same
            ret += all_cnt - cnt[i^j]
        for k in range(i, d+1):
            cnt[i^k] -= 1
            all_cnt -= 1
    return ret
a,b,c,d=map(int,input().split())
print(beautifulQuadruples(a,b,c,d))
