#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : _7_reverse-integer.py
Author       : miaoyc
Create date  : 2020/7/5
Description  : 反转整数
"""

"""
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:
输入: 123
输出: 321

示例 2:
输入: -123
输出: -321

示例 3:
输入: 120
输出: 21

注意:
假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
"""


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        c = 1 if x >= 0 else -1
        tmp_str = str(abs(x))
        tmp_list = [i for i in tmp_str]
        tmp_list.reverse()
        res = int(''.join(tmp_list)) * c
        if res < 2 ** 31 * -1 or res > 2 ** 31 - 1:
            return 0
        else:
            return res
