class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=[set() for _ in range(9)]
        col=[set() for _ in range(9)]
        boxes=[set() for _ in range(9)]
        for r in range(9):
            for c in range(9):
                v=board[r][c]
                if v=='.':
                    continue
                boxindex=(r//3)*3 + (c//3)
                if v in rows[r] or v in col[c] or v in boxes[boxindex]:
                    return False
                rows[r].add(v)
                col[c].add(v)
                boxes[boxindex].add(v)
        return True 