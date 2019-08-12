# -*- coding: utf-8 -*-
"""
Created on

@author: xiaoheizai
"""

'''
反转一个单链表。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        now = head
        while now is not None:
            temp = now.next
            now.next = prev
            prev = now
            now = temp
        return prev