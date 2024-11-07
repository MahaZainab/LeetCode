class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        max_count=0
        for i in range(24):
            count=0
            for num in candidates:
                if(num & (1<<i)) !=0:
                    count +=1
            max_count=max(max_count, count)
        return max_count       