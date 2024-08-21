class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result=[]
        maxCandies=max(candies)
        for i in range(len(candies)):
            result.append(candies[i]+extraCandies>=maxCandies)
        return result