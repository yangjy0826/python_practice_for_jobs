# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if len(pre) == 0 or len(tin) == 0:
            return None
        else:
            root = TreeNode(pre[0])
            p_root = tin.index(pre[0])
            root.left = self.reConstructBinaryTree(pre[1:p_root+1], tin[:p_root])
            root.right = self.reConstructBinaryTree(pre[p_root+1:], tin[p_root+1:])
        return root