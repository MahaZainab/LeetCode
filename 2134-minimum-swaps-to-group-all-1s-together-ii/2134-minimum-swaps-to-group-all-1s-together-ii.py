class Solution:
    def minSwaps(self, nums: List[int]) -> int:
         # Initialize minimum swaps to a large value
        minimum_swaps = float("inf")

        # Calculate the total number of 1s in the array
        total_ones = sum(nums)

        # Initialize the count of 1s in the current window
        ones_count = nums[0]
        end = 0

        # Slide the window across the array
        for start in range(len(nums)):
            # Adjust ones_count by removing the element that
            # is sliding out of the window
            if start != 0:
                ones_count -= nums[start - 1]

            # Expand the window to the right until it reaches the desired size
            while end - start + 1 < total_ones:
                end += 1
                ones_count += nums[end % len(nums)]

            # Update the minimum number of swaps needed
            minimum_swaps = min(minimum_swaps, total_ones - ones_count)

        return minimum_swaps