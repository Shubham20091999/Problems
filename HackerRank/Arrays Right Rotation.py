a=[1,2,3,4,5]
d=len(a)-3
# right rotation by 3
for i in range(d,d+len(a)):
    print(a[i%len(a)])