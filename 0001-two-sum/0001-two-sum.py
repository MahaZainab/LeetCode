class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        for i, num in enumerate(nums):
            complement=target-num
            if complement in hashmap:
                return [hashmap[complement],i]
            
            hashmap[num]=i       
        
        
        
        
        
        
        
        
        
        
        
        # hashmap={}
        # for i in range(len(nums)):
        #     hashmap[i]= target-nums[i]
        # for i in range(len(nums)):
        #     if target+nums[i] is in hashmap:
        #         return i 







        # left=0
        # right=len(nums)-1
        # hashmap={}
        # for i in range(len(nums)):
        #     hasmap[numms[i]]=i
        # nums.sort()
        # for i in range(len(nums)):
        #     print(nums[left], nums[right])
        #     if (nums[left]+nums[right])==target:
        #         return [left,right]
        #     elif (nums[left]+nums[right])>target:
        #         right-=1
        #     else:
        #         left+=1