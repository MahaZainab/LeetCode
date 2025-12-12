class Solution:
    def fib(self, n: int) -> int:
        dp=[0]*(n+1)

        def helper(n, dp)->int:
            if n==0:
                return 0
            if n==1:
                return 1
            if dp[n] !=0:
                return dp[n]
            fib1=self.fib(n-1)
            fib2=self.fib(n-2)
            dp[n]=fib1+fib2
            return dp[n]
        return helper(n, dp)


       

















        # # This is tabulation of the DP
        # if n==0 or n==1:
        #     return n
        # dp=[0]*(n+1)
        # dp[0]=0
        # dp[1]=1
        # for i in range(2, n+1):
        #     dp[i]=dp[i-1]+dp[i-2]
        # return dp[n]

        # dp=[0]*(n+1)
        # def helper(n, dp)->int:
        #     if n==0 or n==1:
        #         return n
        #     if dp[n] !=0:
        #         return dp[n]
        #     dp[n]=helper(n-1, dp) + helper(n-2, dp)
        #     return dp[n]
        # return helper(n, dp)


        # if n<=1:
        #     return n
        # a, b=0,1
        # for i in range(2,n+1):
        #     c=a+b
        #     a=b
        #     b=c
        # return c