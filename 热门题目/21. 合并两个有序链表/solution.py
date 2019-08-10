# -*- coding: utf-8 -*-
"""
Created on

@author: xiaoheizai
"""

'''
将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-two-sorted-lists
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        temp_1 = l1
        temp_2 = l2
        root = ListNode(0)
        temp_3 = root
        while temp_1 is not None and temp_2 is not None:
            if temp_1.val < temp_2.val:
                temp_3.next = temp_1
                temp_1 = temp_1.next
            else:
                temp_3.next = temp_2
                temp_2 = temp_2.next
            temp_3 = temp_3.next
        if temp_1 is not None:
            temp_3.next = temp_1
        elif temp_2 is not None:
            temp_3.next = temp_2
        return root.next