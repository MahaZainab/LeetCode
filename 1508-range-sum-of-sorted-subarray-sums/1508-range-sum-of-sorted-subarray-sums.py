class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        store_subarray = []
        for i in range(len(nums)):
            sum = 0
            # Iterate through all indices ahead of the current index.
            for j in range(i, len(nums)):
                sum += nums[j]
                store_subarray.append(sum)

        # Sort all subarray sum values in increasing order.
        store_subarray.sort()

        # Find the sum of all values between left and right.
        range_sum = 0
        mod = 10**9 + 7
        for i in range(left - 1, right):
            range_sum = (range_sum + store_subarray[i]) % mod
        return range_sum
        