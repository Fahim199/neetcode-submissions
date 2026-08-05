/**
 * Definition for singly-linked list.
 * class ListNode {
 *     constructor(val = 0, next = null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */

class Solution {
    /**
     * @param {ListNode} head
     * @param {number} n
     * @return {ListNode}
     */
    removeNthFromEnd(head, n) {
        let reversedHead = this.reverseList(head);
        if(n==1){
            return this.reverseList(reversedHead.next) 
        }
        let curr = reversedHead;
        for(let i = 0 ; i< n-2; i++){
            curr = curr.next
        }
        curr.next = curr.next.next;
        return this.reverseList(reversedHead)

    }

    reverseList(head){
        let prev = null
        let curr = head
        while(curr){
            let temp = curr.next
            curr.next = prev
            prev= curr
            curr = temp 
        }
        return prev;

    }
}
