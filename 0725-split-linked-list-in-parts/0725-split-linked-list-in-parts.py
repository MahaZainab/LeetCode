class Solution:
    def splitListToParts(
        self, head: Optional[ListNode], k: int
    ) -> List[Optional[ListNode]]:
        ans = [None] * k

        # get total size of linked list
        size = 0
        current = head
        while current is not None:
            size += 1
            current = current.next

        # minimum size for the k parts
        split_size = size // k

        # Remaining nodes after splitting the k parts evenly.
        # These will be distributed to the first (size % k) nodes
        num_remaining_parts = size % k

        current = head
        prev = current
        for i in range(k):
            # create the i-th part
            new_part = current
            # calculate size of i-th part
            current_size = split_size
            if num_remaining_parts > 0:
                num_remaining_parts -= 1
                current_size += 1

            # traverse to end of new part
            j = 0
            while j < current_size:
                prev = current
                if current is not None:
                    current = current.next
                j += 1

            # cut off the rest of linked list
            if prev is not None:
                prev.next = None

            ans[i] = new_part

        return ans