class Solution:
    def divide(self, dividend, divisor):
        sign = -1 if((dividend < 0) ^ (divisor < 0)) else 1
        dividend = abs(dividend)
        divisor = abs(divisor)
        quotient = 0
        # temp=quotient*divisor
        temp = 0

        for i in range(31, -1, -1):
            # divisor<<i equi to divisor*2**i
            # if dividend>divisor*2**10
            # then there will be atleast 2**10
            if (divisor << i <= dividend-temp):
                temp += divisor << i
                quotient |= 1 << i
                print(quotient)

        if(sign == -1):
            return -(quotient if(quotient >> 31 > 0) else 2**31)
        else:
            return (quotient if(quotient >> 31 > 0) else 2**31-1)


Solution().divide(20, 3)
