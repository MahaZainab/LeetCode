class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        ans=[]
        result=[]
        def findPermutation(nums):
            if len(nums)==0:
                result.append(ans[:])
                return
            for i in range(len(nums)):
                ans.append(nums[i])
                num=nums[:i]+nums[i+1:]
                findPermutation(num)
                ans.pop()
        findPermutation(nums)
        return result

        