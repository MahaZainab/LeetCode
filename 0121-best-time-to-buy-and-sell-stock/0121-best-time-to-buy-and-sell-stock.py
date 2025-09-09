class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # The brute force approach where the time complexity will be O(n^2) and space complexity is constant
        # n=len(prices)
        # max_profit=0
        # for i in range(n):
        #     for j in range(i+1, n):
        #         profit= prices[j]-prices[i]
        #         max_profit = max(max_profit, profit)
        # return max_profit
        # The following approach will solve the question in O(n) time and space would be constant again
        left=0
        right=1
        max_profit=0
        for i in range(len(prices)-1):
            if prices[left]<prices[right]:
                profit=prices[right]-prices[left]
                max_profit=max(max_profit, profit)
            else:
                left=right
            right+=1
        return max_profit


        