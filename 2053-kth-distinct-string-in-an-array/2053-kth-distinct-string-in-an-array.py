class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        frequency_map = {}

        # First pass: Populate the frequency map
        for s in arr:
            frequency_map[s] = frequency_map.get(s, 0) + 1

        # Second pass: Find the k-th distinct string
        for s in arr:
            # Check if the current string is distinct
            if frequency_map[s] == 1:
                k -= 1
            # When k reaches 0, we have found the k-th distinct string
            if k == 0:
                return s
        return ""
        