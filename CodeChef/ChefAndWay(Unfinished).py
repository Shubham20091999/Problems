
n,k=map(int,input().split())
l=list(map(int,input().split()))

min=float('inf')

def Try(j,val):
	global min,k,l

	for i in range(j,j+k):
		if(i>=len(l)-1):
			if(val<min):
				min=val
			return
		Try(i+1,val*l[i])

Try(1,1)
print(min*l[0]*l[-1]%1000000007)
