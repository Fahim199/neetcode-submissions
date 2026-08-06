# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head
        curr =head
        cnt = 0;
        while(curr):
            cnt+=1
            curr=curr.next
        
        cnt =cnt - n;

        curr = head

        if(cnt <2):
            if(cnt==0):
                return curr.next
            else:
                curr.next = curr.next.next
                return head
        
        cnt -=1
        for i in range(cnt):
            curr =curr.next
        
        curr.next = curr.next.next

        return head
        