#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : jz-offer2-05-ti-huan-kong-ge.py
Author       : miaoyc
Create date  : 2022/1/4 11:55 下午
Description  : 替换空格
"""

"""
难度：简单

请实现一个函数，把字符串 s 中的每个空格替换成"%20"。
示例 1：
输入：s = "We are happy."
输出："We%20are%20happy."

限制：
0 <= s 的长度 <= 10000
"""


class Solution:
    def replaceSpace(self, s: str) -> str:
        r = ''
        for i in s:
            if i == ' ':
                r = r + '%20'
            else:
                r = r + i
        return r
