# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        slow = fast = head
        while fast and fast.next:
            if fast.val== fast.next.val:
                fast=fast.next
            else:
                slow.next=fast.next
                slow=slow.next
                fast=slow
        #fast=fast.next
        slow.next=fast.next   
        return head

        # while cur and cur.next:
        #     if cur.val== cur.next.val:
        #         cur.next=cur.next.next
        #     else:
        #         cur=cur.next
        # return head
        