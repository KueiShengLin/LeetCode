# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def traversal(self, res, now):
        now_res = res
        if now.left != None:
            now_res = self.traversal(now_res, now.left)
        if now.val != None:
            now_res.append(now.val)
        if now.right != None:
            now_res = self.traversal(now_res, now.right)
                
        return now_res
                
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # LVR
        # It can use stack to handle
        if root == None:
            return []
        ans = self.traversal([], root)
        return ans