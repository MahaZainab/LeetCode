import heapq


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        min_heap = []  # min-heap to store and retrieve the smallest ugly number
        seen_numbers = set()  # set to avoid duplicates
        prime_factors = [2, 3, 5]  # factors for generating new ugly numbers

        heapq.heappush(min_heap, 1)
        seen_numbers.add(1)

        current_ugly = 1
        for _ in range(n):
            current_ugly = heapq.heappop(min_heap)  # get the smallest number

            # generate and push the next ugly numbers
            for prime in prime_factors:
                next_ugly = current_ugly * prime
                if next_ugly not in seen_numbers:  # avoid duplicates
                    heapq.heappush(min_heap, next_ugly)
                    seen_numbers.add(next_ugly)

        return current_ugly  # return the nth ugly number