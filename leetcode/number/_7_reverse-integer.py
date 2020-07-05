#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : _7_reverse-integer.py
Author       : miaoyc
Create date  : 2020/7/5
Description  : 反转整数
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
