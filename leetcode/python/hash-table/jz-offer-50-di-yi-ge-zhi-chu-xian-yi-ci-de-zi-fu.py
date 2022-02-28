#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : jz-offer-50-di-yi-ge-zhi-chu-xian-yi-ci-de-zi-fu.py
Author       : miaoyc
Create date  : 2022/2/28 10:34 PM 
Description  : 第一个只出现一次的字符
"""

"""
难度：简单

在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。

示例 1:
输入：s = "abaccdeff"
输出：'b'

示例 2:
输入：s = "" 
输出：' '

限制：
0 <= s 的长度 <= 50000
"""

from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> str:
        counter = Counter(s)
        for i in s:
            if counter.get(i) == 1:
                return i
        return ' '
