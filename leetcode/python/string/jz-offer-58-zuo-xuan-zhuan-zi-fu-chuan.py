#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : jz-offer-58-zuo-xuan-zhuan-zi-fu-chuan.py
Author       : miaoyc
Create date  : 2022/2/24 12:07 AM
Description  : 左旋转字符串
"""

"""
难度：简单

字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。请定义一个函数实现字符串左旋转操作的功能。比如，输入字符串"abcdefg"和数字2，该函数将返回左旋转两位得到的结果"cdefgab"。

示例 1：
输入: s = "abcdefg", k = 2
输出:"cdefgab"

示例 2：
输入: s = "lrloseumgh", k = 6
输出:"umghlrlose"

限制：
1 <= k < s.length <= 10000
"""

"""
不是，这叫啥题啊，写完有点儿怀疑自己，凑个数吧，最水的题目了。
"""


class Solution(object):
    def reverseLeftWords(self, s, n):
        """
        :type s: str
        :type n: int
        :rtype: str
        """
        return s[n:] + s[:n]
