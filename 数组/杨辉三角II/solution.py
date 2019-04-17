# -*- coding: utf-8 -*-
"""
Created on Apr 13、4

@author: xiaoheizai
"""

'''
description:
给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。
输入: 3
输出: [1,3,3,1]

你可以优化你的算法到 O(k) 空间复杂度吗？ # 没解决
'''


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        else:
            result = [[1]]
            for i in range(1, rowIndex+1):
                temp = [1]
                for j in range(len(result[i-1]) - 1):
                    temp.append(result[i-1][j] + result[i-1][j+1])
                temp.append(1)
                result.append(temp)
            return result[-1]