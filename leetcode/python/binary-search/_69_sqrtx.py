#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : _69_sqrtx.py
Author       : miaoyc
Create date  : 2021/8/24 11:03 下午
Description  : x的平方根
"""

"""
实现int sqrt(int x)函数。
计算并返回x的平方根，其中x 是非负整数。
由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

示例 1:
输入: 4
输出: 2

示例 2:
输入: 8
输出: 2
说明: 8 的平方根是 2.82842..., 
由于返回类型是整数，小数部分将被舍去。
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        low, high, res = 0, x, -1
        while low <= high:
            mid = (low + high) // 2
            if mid*mid <= x:
                res = mid
                low = mid + 1
            else:
                high = mid - 1
        return int(res)
