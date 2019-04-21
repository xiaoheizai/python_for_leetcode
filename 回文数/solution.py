# -*- coding: utf-8 -*-
"""
Created on Apr 13、4

@author: xiaoheizai
"""

'''
description:
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
输入: 121
输出: true

输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
'''
class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)
        i = 0
        j = len(str_x) - 1
        while i < j:
            if str_x[i] != str_x[j]:
                return False
            else:
                i += 1
                j -= 1
        return True