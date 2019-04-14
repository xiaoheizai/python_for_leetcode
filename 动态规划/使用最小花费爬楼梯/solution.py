<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""
Created on Apr 13

@author: xiaoheizai
"""

'''
description:
使用最小花费爬楼梯:数组的每个索引做为一个阶梯，第 i个阶梯对应着一个非负数的体力花费值 cost[i](索引从0开始)。
每当你爬上一个阶梯你都要花费对应的体力花费值，然后你可以选择继续爬一个阶梯或者爬两个阶梯。
您需要找到达到楼层顶部的最低花费。在开始时，你可以选择从索引为 0 或 1 的元素作为初始阶梯。

输入: cost = [10, 15, 20]
输出: 15
解释: 最低花费是从cost[1]开始，然后走两步即可到阶梯顶，一共花费15。

输入: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
输出: 6
解释: 最低花费方式是从cost[0]开始，逐个经过那些1，跳过cost[3]，一共花费6。

动态规划：走到第i个位置的花费值：f(i) = min(f(i-1), f(i-2)) + cost[i]
'''

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        total_cost = []
        total_cost.append(cost[0])
        total_cost.append(cost[1])
        i = 2
        while i < len(cost):
            total_cost.append(min(total_cost[i-1], total_cost[i-2]) + cost[i])
            i += 1
        final_cost = min(total_cost[i-1], total_cost[i-2])
=======
# -*- coding: utf-8 -*-
"""
Created on Apr 13

@author: xiaoheizai
"""

'''
description:
使用最小花费爬楼梯:数组的每个索引做为一个阶梯，第 i个阶梯对应着一个非负数的体力花费值 cost[i](索引从0开始)。
每当你爬上一个阶梯你都要花费对应的体力花费值，然后你可以选择继续爬一个阶梯或者爬两个阶梯。
您需要找到达到楼层顶部的最低花费。在开始时，你可以选择从索引为 0 或 1 的元素作为初始阶梯。

输入: cost = [10, 15, 20]
输出: 15
解释: 最低花费是从cost[1]开始，然后走两步即可到阶梯顶，一共花费15。

输入: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
输出: 6
解释: 最低花费方式是从cost[0]开始，逐个经过那些1，跳过cost[3]，一共花费6。

动态规划：走到第i个位置的花费值：f(i) = min(f(i-1), f(i-2)) + cost[i]
'''

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        total_cost = []
        total_cost.append(cost[0])
        total_cost.append(cost[1])
        i = 2
        while i < len(cost):
            total_cost.append(min(total_cost[i-1], total_cost[i-2]) + cost[i])
            i += 1
        final_cost = min(total_cost[i-1], total_cost[i-2])
>>>>>>> 动态规划题目
        return final_cost