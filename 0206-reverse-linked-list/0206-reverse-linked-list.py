# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        prev=None
        curr=nextNode=head
        while curr:
            nextNode=curr.next
            curr.next=prev
            prev=curr
            curr=nextNode
        head=prev
        return head

        # if not head:
        #     return None
        # prev = None
        # cur=nextNode=head
        # while cur:
        #     nextNode=cur.next
        #     cur.next=prev
        #     prev=cur
        #     cur=nextNode
        # head=prev
        # return head

        # if not head:
        #     return None

        # newHead = head
        # if head.next:
        #     newHead = self.reverseList(head.next)
        #     head.next.next = head
        # head.next = None
        
        # return newHead