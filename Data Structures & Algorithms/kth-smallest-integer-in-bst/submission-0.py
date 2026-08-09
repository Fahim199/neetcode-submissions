# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res, cnt = 0, k;
        def inOrder(node,rem):
            nonlocal res, cnt;
            if not node:
                return
            
            inOrder(node.left, rem)
            cnt-=1
            if cnt == 0:
                res = node.val
                return
            inOrder(node.right, rem)
        
        inOrder(root, cnt)
        return res

        