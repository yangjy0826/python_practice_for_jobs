# 题目来自剑指offer
# 输入一个链表，从尾到头打印链表每个节点的值。
# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def __init__(self, listNode):
        self.listNode = listNode

    def printListFromTailToHead(self):
        # write code here
        list_t2h = []
        head = listNode
        while head:
            list_t2h.append(head.val)
            head = head.next
        list_t2h.reverse()
        return list_t2h
