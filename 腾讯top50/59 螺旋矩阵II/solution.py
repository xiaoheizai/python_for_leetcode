# -*- coding: utf-8 -*-
"""
Created on Apr 13、4

@author: xiaoheizai
"""

'''
给定一个正整数 n，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。

示例:

输入: 3
输出:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/spiral-matrix-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        l, r, t, b = 0, n-1, 0, n-1
        mat = [[0] * n for _ in range(n)]
        num, final_num = 1, n * n
        while num <= final_num:
            for i in range(l, r+1):
                mat[t][i] = num
                num += 1
            t += 1
            for i in range(t, b+1):
                mat[i][r] = num
                num += 1
            r -= 1
            for i in range(r, l-1, -1):
                mat[b][i] = num
                num += 1
            b -= 1
            for i in range(b, t-1, -1):
                mat[i][l] = num
                num += 1
            l += 1
        return mat