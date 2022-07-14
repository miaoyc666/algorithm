#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : _172_factorial-trailing-zeroes.py
Author       : miaoyc
Create date  : 2021/8/12 23:44
Description  : 阶乘后的零
"""

"""
给定一个整数 n，返回 n! 结果尾数中零的数量。

示例 1:

输入: 3
输出: 0
解释:3! = 6, 尾数中没有零。
示例2:

输入: 5
输出: 1
解释:5! = 120, 尾数中有 1 个零.
说明: 你算法的时间复杂度应为O(logn)。
"""


class Solution:
    def trailingZeroes(self, n: int) -> int:
        # 统计因数5的个数
        count = 0
        for i in range(1, n+1):
            if i % 5 == 0:
                num = i
                while num % 5 == 0 and num >= 5:
                    count += 1
                    num /= 5
        return count
