#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : _121_best-time-to-buy-and-sell-stock.py
Author       : miaoyc
Create time  : 2020/7/22 11:06
Update time  : 2024/1/10 10:44
Description  : 买卖股票的最佳时机
"""

"""
给定一个数组，它的第i 个元素是一支给定股票第 i 天的价格。
如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），设计一个算法来计算你所能获取的最大利润。
注意：你不能在买入股票前卖出股票。

示例 1:
输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。

示例 2:
输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。

提示：
1 <= prices.length <= 105
0 <= prices[i] <= 104
"""

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        # 1. 记录【今天之前买入的最小市值和最大盈利】
        min_v = prices[0]
        max_v = 0
        # 跳过第一天，从第二天开始迭代计算
        for i in range(1, len(prices)):
            # 2.计算【今天之前最小值买入，今天卖出的获利】，也即【今天卖出的最大获利】
            tmp_max_v = prices[i] - min_v
            # 更新最小市值
            min_v = min(prices[i], min_v)
            # 3.比较【每天的最大获利】，取最大值即可，完成循环
            max_v = max(max_v, tmp_max_v)
        return max_v
