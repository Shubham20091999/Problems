# https://www.hackerrank.com/challenges/short-palindrome/problem

# string = input()
# M=(10**9+7)
# # freqLeft = [0]*sz
# # # Saving frequencies of letters to the left of the ith letter
# # for s in range(3):
# #     freqLeft[ord(string[s])-97] += 1

# count = 0
# for l in range(0, len(string)-3):
#     freqLeft = [0]*sz
#     for s in range(l,l+3):
#         freqLeft[ord(string[s])-97] += 1
#     freqLeft[ord(string[l])-97] -= 1
#     for r in range(l+3, len(string)):
#         if(string[l] == string[r]):
#             for i in range(sz):
#                 freq = freqLeft[i]
#                 if(freq > 1):
#                     count += (freq*(freq-1)//2)%M
#         freqLeft[ord(string[r])-97] += 1
# print(count%M)



sz=2
# Num of times a character occured upto ith term
c1=[0 for _ in range(sz)]

# mth row and nth col
# ith charter means the ith position in alphabets (1st char=a)

# For iter upto jth term
# shows how many pairs of mth char and nth chars are possible
# till the last occurence of nth character in the string including character at jth position
c2=[[0 for _ in range(sz) ] for _ in range(sz)]

# 
c3=[[0 for _ in range(sz)] for _ in range(sz)]


counter=0
s=input()
for j in range(len(s)):
    c = ord(s[j]) - ord('a')
    for i in range(sz):
        # counter += c3[c][i]           
        c3[i][c] += c2[i][c]             
        c2[i][c] += c1[i] 
    c1[c] += 1
print(counter%(10**9+7))

# this is till jth term in the string 
# character is {b}
# Occurence {b} is saved in c1
# Occurence {b}{a} are saved in c2
# Occurence {b}{a}{a} is saved in c3
# Save the number of pairs for {b}{a}{a} that is occuring
# if current character is {b} then add thaose occurence to the count