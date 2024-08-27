class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows=len(matrix)
        columns=len(matrix[0])
        transMat=[]
        for i in range(columns):
            zero=[0]*rows
            transMat.append(zero.copy())
        print(transMat)
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                transMat[j][i]=matrix[i][j]
        return transMat
        