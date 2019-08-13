# -*- coding: utf-8 -*-
"""
Created on

@author: xiaoheizai
"""

'''
编写一个程序，找到两个单链表相交的起始节点。

'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None
        temp_1 = headA
        temp_2 = headB
        while temp_1 is not temp_2:
            if temp_1 is not None:
                temp_1 = temp_1.next
            else:
                temp_1 = headB
            if temp_2 is not None:
                temp_2 = temp_2.next
            else:
                temp_2 = headA
        return temp_1