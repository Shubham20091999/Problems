class Solution:
    def intToRoman(self, num: int) -> str:
        N=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
        G=['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
        ans=''
        for i,n in enumerate(N):
            if(num>=n):
                rem=num//n
                ans+=''.join([G[i]]*(rem))
                num-=((rem)*n)
        return ans