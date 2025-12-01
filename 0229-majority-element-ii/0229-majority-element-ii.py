class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        numpair={}
        count=len(nums)//3
        output=[]
        for num in nums:
            if num in numpair:
                numpair[num]+=1
            else:
                numpair[num]=1
        for num, c in numpair.items():
            if c>count:
                output.append(num)
        return output