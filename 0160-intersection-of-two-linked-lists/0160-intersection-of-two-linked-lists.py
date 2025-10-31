# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None
        currA=headA
        currB=headB
        lenA=0
        lenB=0
        diff=0
        while currA:
            lenA+=1
            currA=currA.next
        while currB:
            lenB+=1
            currB=currB.next
        currA=headA
        currB=headB
        if lenA>lenB:
            diff=lenA-lenB
            while diff>0:
                currA=currA.next
                diff-=1
        if lenB>lenA:
            diff=lenB-lenA
            while diff>0:
                currB=currB.next
                diff-=1
        while currA or currB:
            if currA==currB:
                return currA
            currA=currA.next
            currB=currB.next
        return None

        
        

        