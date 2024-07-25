class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) > 1:
            mid = len(nums) // 2  # Finding the mid of the array
            left_half = nums[:mid]  # Dividing the elements into 2 halves
            right_half = nums[mid:]

            self.sortArray(left_half)  # Sorting the first half
            self.sortArray(right_half)  # Sorting the second half

            i = j = k = 0

        # Copy data to temp arrays left_half[] and right_half[]
            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    nums[k] = left_half[i]
                    i += 1
                else:
                    nums[k] = right_half[j]
                    j += 1
                k += 1

        # Checking if any element was left
            while i < len(left_half):
                nums[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                nums[k] = right_half[j]
                j += 1
                k += 1

        return nums
        