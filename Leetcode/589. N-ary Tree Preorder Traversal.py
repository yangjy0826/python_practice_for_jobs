# Given an n-ary tree, return the preorder traversal of its nodes' values.
# The 1st solution:
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root is None:
            return []

        stack, output = [root, ], []
        while stack:
            root = stack.pop()
            output.append(root.val)
            stack.extend(root.children[::-1])
            # extend children的顺序是反过来的，因为堆栈是先进后出，我们为了保证pop的顺序而将其颠倒
        return output
# The 2nd solution:
# """
# # Definition for a Node.
# class Node(object):
#     def __init__(self, val, children):
#         self.val = val
#         self.children = children
# """
# class Solution(object):
#     def preorder(self, root):
#         """
#         :type root: Node
#         :rtype: List[int]
#         """
#         def dfs(root):
#             if not root:
#                 return
#             res.append(root.val)
#             for c in root.children:
#                 dfs(c)
#
#         res = []
#         dfs(root)
#         return res​
