class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2:
            return []
        smallmap={}
        result=[]
        if len(nums1)<len(nums2) or len(nums1) == len(nums2):
            for num in nums1:
                smallmap[num]=smallmap.get(num, 0) + 1
        else:
            for num in nums2:
                smallmap[num]=smallmap.get(num, 0) + 1
        
        if len(nums1)>len(nums2):
            for num in nums1:
                if num in smallmap:
                    count=smallmap.get(num)
                    result.append(num)
                    smallmap[num]=count-1
                    if smallmap[num]<=0:
                        smallmap.pop(num)
        else:
            for num in nums2:
                if num in smallmap:
                    count=smallmap.get(num)
                    result.append(num)
                    smallmap[num]=count-1
                    if smallmap[num]<=0:
                        smallmap.pop(num)
        return result
        
                
        

            