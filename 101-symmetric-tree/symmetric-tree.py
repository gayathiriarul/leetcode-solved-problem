# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
 
class Solution:
    def isSymmetric(self, root):

        def check(a, b):
            if not a and not b:
                return True

            if not a or not b:
                return False

            return (a.val == b.val and
                    check(a.left, b.right) and
                    check(a.right, b.left))

        return check(root.left, root.right)