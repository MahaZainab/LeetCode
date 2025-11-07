class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        result=0
        cost=1
        degrees=[0]*n
        for road in roads:
            degrees[road[0]]+=1
            degrees[road[1]]+=1
        degrees.sort()
        for degree in degrees:
            result += degree*cost
            cost+=1
        return result 
        