<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""
Created on Apr 13

@author: xiaoheizai
"""

'''
description:
爬楼梯:假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
注意：给定 n 是一个正整数。

输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶

输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶
'''


class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        a1 = 1
        a2 = 2
        i = 3
        while i <= n:
            temp = a2
            a2 = a1 + a2
            a1 = temp
            i += 1
=======
# -*- coding: utf-8 -*-
"""
Created on Apr 13

@author: xiaoheizai
"""

'''
description:
爬楼梯:假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
注意：给定 n 是一个正整数。

输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶

输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶

动态规划：爬上第n阶楼梯的公式 f(n) = f(n-2) + f(n-1)
'''


class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        a1 = 1
        a2 = 2
        i = 3
        while i <= n:
            temp = a2
            a2 = a1 + a2
            a1 = temp
            i += 1
>>>>>>> 动态规划题目
        return a2