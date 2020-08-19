# https://www.hackerrank.com/challenges/validating-credit-card-number/problem

def isValid(s: str):
    if(s[0] == '4' or s[0] == '5' or s[0] == '6'):  # Checking if first number is 4,5 or 6
        if(len(s) == 19):  # Checking if number is '-' seperated
            if(s[4] == s[9] == s[14] == '-'):#Checking if '-' occure ar 5th,9th and 14th position(equally distant)
                s = s.replace('-', '')  # removing '-'s from the number
            else:
                return False
        if(len(s) != 16):#Checking is the number if 16 digits long
            return False

        l = 0  # Continious len
        for i in range(1, len(s)):
            c = s[i]
            #ord gives ascii value of the letter (48 is for 0 and 57 is for 9)
            if(ord(c) < 48 or ord(c) > 57):#Checking if all numbers are between 0 and 9
                return False

            #Continuity check
            if(s[i] == s[i-1]):
                l += 1#increasing by one if current number is equal to previous number
            else:
                l = 0
            if(l >= 3): #checking if the length of continuity is 3
                #consider 5555 here l will be equal to 3 when it gets to last 5
                return False

        return True
    else:
        return False


for _ in range(int(input())):
    print("Valid" if isValid(input()) else "Invalid")


# --------------------

# import re
# def isValid(s):
#     if(re.fullmatch(r"[456]\d{3}(-?\d{4}){3}", s) and not re.search(r"(\d)\1{3}", s.replace('-', ''))):
#         return True
#     return False


# for i in range(int(input())):
#     print("Valid" if isValid(input()) else "Invalid")
