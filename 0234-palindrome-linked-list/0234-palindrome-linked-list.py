# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        # Find Middle
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        # reverse second half
        cur=slow
        prev=None
        while cur:
            nextNode=cur.next
            cur.next=prev
            prev=cur
            cur=nextNode
        right=prev
        left=head
        while right:
            if left.val != right.val:
                return False
            left=left.next
            right=right.next
        return True




        