# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return

        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        

        secondHalf = slow.next
        slow.next = prev = None

        #reversing the linked list
        while secondHalf:
            tmp = secondHalf.next
            secondHalf.next = prev
            prev  = secondHalf
            secondHalf = tmp

    
        firstHalf, secondHalf = head,  prev

        while secondHalf:
            tmp1, tmp2 = firstHalf.next, secondHalf.next
            firstHalf.next = secondHalf
            secondHalf.next = tmp1
            firstHalf, secondHalf = tmp1, tmp2

        
