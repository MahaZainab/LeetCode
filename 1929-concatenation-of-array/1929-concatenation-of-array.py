class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        #ans=nums+nums
        #return ans
        #return nums+nums
        nums.extend(nums)
        return nums
        