class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
    
        startRow, startCol = 0, 0
        endRow, endCol = len(matrix) - 1, len(matrix[0]) - 1
    
        while startRow <= endRow and startCol <= endCol:
        
        # ---- top row (left → right) ----
            for i in range(startCol, endCol + 1):
                result.append(matrix[startRow][i])
        
        # ---- right column (top → bottom) ----
            for j in range(startRow + 1, endRow + 1):
                result.append(matrix[j][endCol])
        
        # ---- bottom row (right → left) ----
            if startRow != endRow:  # avoid double counting
                for i in range(endCol - 1, startCol - 1, -1):
                    result.append(matrix[endRow][i])
        
        # ---- left column (bottom → top) ----
            if startCol != endCol:  # avoid double counting
                for j in range(endRow - 1, startRow, -1):
                    result.append(matrix[j][startCol])
        
        # move boundaries inward
            startRow += 1
            endRow -= 1
            startCol += 1
            endCol -= 1
    
        return result
