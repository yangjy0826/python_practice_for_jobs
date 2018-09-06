# My code beats 90% of the submissions
# 注意一下这个trick，已经return之后，函数后面的行就不会再运算了 比if……elif……else的模型（速度只打败了10%）快好多
class Solution:
    def mergeTrees(self, t1, t2): ##recursion
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 == None:
            return t2
        if t2 == None:
            return t1
        if t1 == None and t2 == None:
            return None
        t1.val += t2.val
        t1.left = self.mergeTrees(t1.left,t2.left)
        t1.right = self.mergeTrees(t1.right,t2.right)
        return t1
