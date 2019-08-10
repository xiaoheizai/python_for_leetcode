# -*- coding: utf-8 -*-
"""
Created on

@author: xiaoheizai
"""

'''
给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。

例如，给出 n = 3，生成结果为：

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/generate-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return []
        result = [[""]]
        for i in range(1, n+1):
            temp = []
            for j in range(i):
                temp_1 = result[j]
                temp_2 = result[i-1-j]
                for value_1 in temp_1:
                    for value_2 in temp_2:
                        temp_new = "(" + value_1 + ")" + value_2
                        temp.append(temp_new)
            result.append(temp)
        return result[n]