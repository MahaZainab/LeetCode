class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in range(len(nums)):
            #index=nums[i]
            ans.append(nums[nums[i]])
        return ans
        