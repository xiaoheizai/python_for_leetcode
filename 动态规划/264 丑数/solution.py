# -*- coding: utf-8 -*-
"""
Created on

@author: xiaoheizai
"""

'''
编写一个程序，找出第 n 个丑数。

丑数就是只包含质因数 2, 3, 5 的正整数。

示例:

输入: n = 10
输出: 12
解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
说明:  

1 是丑数。
n 不超过1690。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ugly-number-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        ugly_list = [1]
        i = 0
        j = 0
        t = 0
        k = 1
        while k < n:
            new_ugly = min(ugly_list[i]*2, ugly_list[j]*3, ugly_list[t]*5)
            if new_ugly == ugly_list[i]*2:
                i += 1
            if new_ugly == ugly_list[j]*3:
                j += 1
            if new_ugly == ugly_list[t]*5:
                t += 1
            ugly_list.append(new_ugly)
            k += 1
        return ugly_list[-1]