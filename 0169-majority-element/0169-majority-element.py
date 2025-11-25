class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numpair={}
        count=len(nums)//2
        for num in nums:
            if num in numpair:
                numpair[num]+=1
            else:
                numpair[num]=1
            if numpair[num]>count:
                return num
        