# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder or not postorder:
            return None

        last_value = postorder.pop() # For postorder traversal the last value is a root
        root = TreeNode(last_value)
        indexAt_inorder = inorder.index(root.val) # 해당 값을 inorder에서 찾기

        root.right = self.buildTree(inorder[indexAt_inorder+1:], postorder)
        root.left = self.buildTree(inorder[:indexAt_inorder], postorder)

        return root