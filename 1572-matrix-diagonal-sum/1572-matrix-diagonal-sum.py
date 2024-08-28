class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum=0
        rows=len(mat)
        for i in range(rows):
            sum+= mat[i][i]
            if i !=rows-1-i:
                sum+= mat[i][rows-1-i]
        return sum