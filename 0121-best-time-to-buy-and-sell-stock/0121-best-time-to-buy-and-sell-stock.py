class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right=0,1
        MaxProfit=0
        while right<len(prices):
            if prices[right]>prices[left]:
                profit=prices[right]-prices[left]
                MaxProfit=max(profit, MaxProfit)
                
            else:
                left=right
            right+=1
        return MaxProfit
