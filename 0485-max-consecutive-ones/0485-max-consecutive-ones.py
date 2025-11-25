class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        countOne=0
        maxc=0
        for num in nums:
            if num==1:
                countOne+=1
                maxc=max(maxc, countOne)
            else:
                countOne=0
        return maxc 
        