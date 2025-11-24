class Solution:
    def countOdds(self, low: int, high: int) -> int:
        diff=high-low
        result=diff//2
        if low%2==1 or high%2==1:
            result+=1
        return result
        