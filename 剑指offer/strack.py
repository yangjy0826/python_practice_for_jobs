# 用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。

# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def push(self, node):  # 堆栈与队列的push是一致的，都在顶部操作
        # write code here
        self.stack1.append(node)
    def pop(self):  # 堆栈的POP也在顶部操作，但是队列的POP在底部操作部
        # return xx
        while len(self.stack1)!=0:  # 先把栈1的内容压入栈2
            self.stack2.append(self.stack1.pop())  # 这里调用的是python自带的pop函数，不是递归
        pop_out = self.stack2.pop()  #  弹出栈2的顶
        while len(self.stack2)!=0:  #  最后把栈2的内容再折回到栈1，栈2空
            self.stack1.append(self.stack2.pop())
        return pop_out
