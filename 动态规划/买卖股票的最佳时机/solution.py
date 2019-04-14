# -*- coding: utf-8 -*-
"""
Created on Apr 13

@author: xiaoheizai
"""

'''
description:
买卖股票的最佳时机:给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。
注意你不能在买入股票前卖出股票。

输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。

输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。

动态规划 前i天的最大收益 = max{前i-1天的最大收益，第i天的价格-前i-1天中的最小价格}

'''


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = []
        min_price = float("inf")
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            temp_profit = prices[i] - min_price
            if i == 0:
                profit.append(0)
            elif temp_profit > profit[i-1]:
                profit.append(temp_profit)
            else:
                profit.append(profit[i-1])
        if len(profit) == 0:
            return 0
        else:
			return profit[-1]
