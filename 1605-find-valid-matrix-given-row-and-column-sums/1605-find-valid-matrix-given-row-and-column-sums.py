class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        matrix = [[0] * len(colSum) for _ in range(len(rowSum))]
    
    # Iterate over each cell in the matrix
        for i in range(len(rowSum)):
            for j in range(len(colSum)):
            # Assign the minimum value of rowSum[i] and colSum[j]
                value = min(rowSum[i], colSum[j])
                matrix[i][j] = value
            
            # Subtract the assigned value from rowSum[i] and colSum[j]
                rowSum[i] -= value
                colSum[j] -= value
    
        return matrix


        