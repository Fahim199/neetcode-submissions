# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        resArr = []
        if not root:
            return resArr

        queue = deque([root])

        while queue:
            treeArr = []
            for i in range(len(queue)):
                node = queue.popleft()
                treeArr.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            
            resArr.append(treeArr)
        
        return resArr
        