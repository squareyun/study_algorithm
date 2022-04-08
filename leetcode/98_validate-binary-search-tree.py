# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def check(root, lower, upper):
            if not root:
                return True
            
            if lower < root.val and root.val < upper:
                return check(root.left, lower, root.val) and check(root.right, root.val, upper)
            else: return False
        
        return check(root, float('-inf'), float('inf'))