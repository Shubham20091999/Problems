def MakeNumStr(num):
    ans=[]
    if(num>=10):
        ans=str(num)
    elif(num<10):
        ans=str(0)+str(num)
    return ans

def timeConversion(s):
    hour=int(s[0])*10+int(s[1])
    if(s[8]=='P'):
        if(hour!=12):
            hour+=12
    else:
        if(hour==12):
            hour=0
    hour=MakeNumStr(hour)
    s=s[2:-2]

    s=hour+s
    return s
    
print(timeConversion("12:00:00AM"))

        