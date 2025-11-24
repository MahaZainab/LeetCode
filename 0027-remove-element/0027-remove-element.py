class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        valuecount=0
        kcount=0
        for i in range(len(nums)):
            if nums[i]==val:
                valuecount+=1
            else:
                kcount+=1
                nums[i-valuecount]=nums[i]
            
        return kcount