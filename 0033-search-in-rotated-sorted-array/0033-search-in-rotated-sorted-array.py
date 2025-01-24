class Solution:
    def search(self, nums: List[int], target: int) -> int:
        first=0
        last=len(nums)-1
        while (first<last):
            mid=(first+last)//2
            if nums[mid]>nums[last]:
                first=mid+1
            else:
                last=mid
        pivot=first
        first=0
        last=len(nums)-1

        if target>=nums[pivot] and target<=nums[last]:
            first=pivot
        else:
            last=pivot-1

        while first<= last:
            mid= (first+last)//2
            if nums[mid]== target:
                return mid
            elif nums[mid]<target:
                first=mid+1
            else:
                last=mid-1
        return -1

