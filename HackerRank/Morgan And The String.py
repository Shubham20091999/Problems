def morgan(a, b):
    # So that if one string get over we go for the other string
    # lower case z is used cuz
    # 'z'<'ZA' ==> False
    a += 'z'
    b += 'z'
    ans=[]
    for i in range(len(a) + len(b) - 2):
        if a < b:
            ans.append(a[0])
            a = a[1:]
        else:
            ans.append(b[0])
            b = b[1:]
    return ans

def morganAndString(a, b):
    return ''.join(morgan(a, b))

for _ in range(int(input())):
    print(morganAndString(input(), input()))