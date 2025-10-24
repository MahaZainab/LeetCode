# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less_than_x = ListNode(-1)
        greater_or_equal = ListNode(-1)
    
        # Pointers to track the current end of each list
        current_less = less_than_x
        current_greater = greater_or_equal
    
        current = head
    
        while current:
            if current.val < x:
                # Add to "less than x" list
                current_less.next = current
                current_less = current_less.next
            else:
                # Add to "greater or equal to x" list
                current_greater.next = current
                current_greater = current_greater.next
        
            # Move to next node in original list
            current = current.next
    
        # Connect the two lists: less_than_x -> greater_or_equal
        current_less.next = greater_or_equal.next
    
        # Ensure the final node points to nothing
        current_greater.next = None
    
        # Return the combined list (skip the dummy starter node)
        return less_than_x.next 
        