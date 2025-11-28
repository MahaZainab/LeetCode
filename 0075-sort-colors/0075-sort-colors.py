class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start=0
        end=len(nums)-1
        i=0
        while  i <=end:
            if nums[i]==0:
                temp=nums[start]
                nums[start]=nums[i]
                nums[i]=temp
                start+=1
                i+=1
            elif nums[i]==2:
                temp=nums[end]
                nums[end]=nums[i]
                nums[i]=temp
                end-=1
            else:
                i+=1

        