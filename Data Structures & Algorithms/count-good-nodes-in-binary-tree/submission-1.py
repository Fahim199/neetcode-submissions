# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good = 0

        def dfs(root, maximum):
            nonlocal good
            if not root:
                return

            
            maximum = max(root.val, maximum)
            if root.val >= maximum:
                good+=1
            

            dfs(root.left, maximum)
            dfs(root.right, maximum)

        dfs(root,float("-inf"))
        return good
        