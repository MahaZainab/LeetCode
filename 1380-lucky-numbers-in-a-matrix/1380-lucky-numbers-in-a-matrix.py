class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
         # Find the minimum in each row
        min_in_rows = {min(row) for row in matrix}
    
    # Transpose the matrix to get the columns as rows
        transpose_matrix = list(zip(*matrix))
    
    # Find the maximum in each column
        max_in_columns = {max(col) for col in transpose_matrix}
    
    # The lucky numbers are those which are in both sets
        lucky_nums = list(min_in_rows & max_in_columns)
    
        return lucky_nums

        