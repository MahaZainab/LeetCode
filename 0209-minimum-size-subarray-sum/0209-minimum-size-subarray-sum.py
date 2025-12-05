class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left,right=0,0
        ssum=0
        minLength=float('inf')
        for right in range(len(nums)):
            ssum+=nums[right]
            while ssum>=target:
                minLength=min(minLength, right-left+1)
                ssum-=nums[left]
                left+=1
            right+=1
        return 0 if minLength==float('inf') else minLength


        