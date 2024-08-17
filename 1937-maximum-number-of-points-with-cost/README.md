
# Maximum Number of Points with Cost

## Problem Description

You are given an `m x n` integer matrix `points`. Starting with `0` points, you want to maximize the number of points you can get from the matrix.

- You must pick one cell in each row.
- Picking the cell at coordinates `(r, c)` will add `points[r][c]` to your score.
- However, moving to a cell in the next row that is far from the previous cell will incur a penalty. The penalty is defined as the absolute difference between the column indices of the two cells.

The goal is to find the maximum number of points you can achieve.

### Example

Given a matrix:

```
points = [
    [1, 2, 3],
    [1, 5, 1],
    [3, 1, 1]
]
```

The maximum points you can achieve is `9` by picking cells at `(0, 2)`, `(1, 1)`, and `(2, 0)`.

## Solution Approach

### Dynamic Programming (DP)

We can solve this problem using a dynamic programming approach. Here's how:

### Step 1: Define the DP Table

Let `dp[r][c]` represent the maximum points that can be obtained if you end up in cell `(r, c)` in the `r`-th row.

### Step 2: Base Case

For the first row, the DP values are simply the values in the first row of the matrix because there is no penalty for the first choice:
```python
dp[0][c] = points[0][c]
```

### Step 3: Recurrence Relation

For each subsequent row `r`, calculate `dp[r][c]` as follows:
```python
dp[r][c] = max(dp[r-1][k] - abs(k - c)) + points[r][c] for all k in range(n)
```
However, directly computing this for each cell would be too slow, so we optimize it using left-to-right and right-to-left sweeps.

### Step 4: Optimization with Two Sweeps

- **Left to Right Sweep**: This considers the best possible values when moving from the leftmost column towards the right.
- **Right to Left Sweep**: This considers the best possible values when moving from the rightmost column towards the left.

This reduces the time complexity of our solution to `O(m * n)`.

### Step 5: Final Result

After processing all rows, the maximum value in `dp` will give you the maximum points achievable.

### Pseudocode

```python
def maxPoints(points):
    m, n = len(points), len(points[0])
    
    # DP array initialization
    dp = points[0]
    
    for r in range(1, m):
        # Left to right sweep
        left_max = [0] * n
        left_max[0] = dp[0]
        for c in range(1, n):
            left_max[c] = max(left_max[c-1] - 1, dp[c])
        
        # Right to left sweep
        right_max = [0] * n
        right_max[-1] = dp[-1]
        for c in range(n-2, -1, -1):
            right_max[c] = max(right_max[c+1] - 1, dp[c])
        
        # Update dp for the current row
        for c in range(n):
            dp[c] = points[r][c] + max(left_max[c], right_max[c])
    
    return max(dp)
```

### Complexity Analysis

- **Time Complexity**: `O(m * n)` where `m` is the number of rows and `n` is the number of columns.
- **Space Complexity**: `O(n)` since we only keep the current and previous row's DP values.

## How to Use

1. Implement the provided Python function in your codebase.
2. Call the function `maxPoints(points)` with your matrix `points`.
3. The function will return the maximum points you can achieve.

## Example

```python
points = [
    [1, 2, 3],
    [1, 5, 1],
    [3, 1, 1]
]

print(maxPoints(points))  # Output: 9
```


This dynamic programming approach efficiently calculates the maximum points achievable in the matrix by considering both the points at each cell and the penalties incurred when moving between cells in adjacent rows.
