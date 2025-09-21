# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # First calculate the size
        size=0
        temp=head
        while temp:
            size += 1
            temp=temp.next
        if size==n:
            return head.next
        deleteToBe=size-n
        prev=head
        dummy=prev
        for i in range(deleteToBe-1):
            prev=prev.next
        prev.next=prev.next.next
        return dummy
        # N = 0
        # cur = head
        # while cur:
        #     N += 1
        #     cur = cur.next
        
        # removeIndex = N - n
        # if removeIndex == 0:
        #     return head.next
        
        # cur = head
        # for i in range(N - 1):
        #     if (i + 1) == removeIndex:
        #         cur.next = cur.next.next
        #         break
        #     cur = cur.next
        # return head