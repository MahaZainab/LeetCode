class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mappair={}
        count=len(nums)//2
        for num in nums:
            if num in mappair:
                mappair[num] +=1
            else:
                mappair[num] = 1
            if mappair[num]>count:
                return num

        