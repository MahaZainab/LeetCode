class Solution:
    def findMin(self, nums: List[int]) -> int:
        first=0
        last=len(nums)-1
        while(first<last):
            mid=(first+last)//2
            if nums[mid]>nums[last]:
                first=mid+1
            else:
                last=mid
        return nums[first]