I=int(input())
Odd=["Odd","Even","Even","Odd"]
Even=["Even","Odd","Odd","Even"]
for i in range(0,I):
    l,r=map(int,input().split())
    if(l%2==0):
        print(Even[int((r-l+1)%4-1)])
    else:
        print(Odd[int((r-l)%4-1)])
    
    
    


