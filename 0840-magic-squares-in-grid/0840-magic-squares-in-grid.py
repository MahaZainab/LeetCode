class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        ans = 0
        m = len(grid)
        n = len(grid[0])
        for row in range(m - 2):
            for col in range(n - 2):
                if self._isMagicSquare(grid, row, col):
                    ans += 1
        return ans

    def _isMagicSquare(self, grid, row, col):
        # The sequences are each repeated twice to account for
        # the different possible starting points of the sequence
        # in the magic square
        sequence = "2943816729438167"
        sequenceReversed = "7618349276183492"

        border = []
        # Flattened indices for bordering elements of 3x3 grid
        borderIndices = [0, 1, 2, 5, 8, 7, 6, 3]
        for i in borderIndices:
            num = grid[row + i // 3][col + (i % 3)]
            border.append(str(num))

        borderConverted = "".join(border)

        # Make sure the sequence starts at one of the corners
        return (
            grid[row][col] % 2 == 0
            and (
                sequence.find(borderConverted) != -1
                or sequenceReversed.find(borderConverted) != -1
            )
            and grid[row + 1][col + 1] == 5
        )