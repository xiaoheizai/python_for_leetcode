# -*- coding: utf-8 -*-
"""
Created on

@author: xiaoheizai
"""

'''
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        temp_stack = []
        for value in s:
            if value == "(" or value == "[" or value == "{":
                temp_stack.append(value)
            elif value == ")" or  value == "]" or value == "}":
                if len(temp_stack) == 0:
                    return False
                stack_value = temp_stack.pop()
                if value == ")":
                    if stack_value == "(":
                        continue
                    else:
                        return False
                elif value == "]":
                    if stack_value == "[":
                        continue
                    else:
                        return False
                elif value == "}":
                    if stack_value == "{":
                        continue
                    else:
                        return False
        if len(temp_stack) == 0:
            return True
        else:
            return False