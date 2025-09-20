#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        size=0
        temp=head
        while temp:
            size+=1
            temp=temp.next
        middle=size//2
        for i in range(middle):
            head=head.next
        return head
        