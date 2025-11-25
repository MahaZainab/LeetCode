class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        sortednums=sorted(nums)
        result=[]
        for i in range(len(sortednums)):
            if sortednums[i]==target:
                result.append(i)
        return result
        