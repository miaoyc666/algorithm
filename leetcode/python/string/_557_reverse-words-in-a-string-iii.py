#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : _557_reverse-words-in-a-string-iii.py
Author       : miaoyc
Create date  : 2021/7/22 3:18 上午
Description  : 反转字符串中的单词 III
"""

"""
给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。

示例：

输入："Let's take LeetCode contest"
输出："s'teL ekat edoCteeL tsetnoc"

提示：

在字符串中，每个单词由单个空格分隔，并且字符串中不会有任何额外的空格。
"""


class Solution(object):

    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        tmp = []
        result = ""
        for i in s:
            if i != " ":
                tmp.append(i)
            else:
                result = result + self.reverseString(tmp) + " "
                tmp = []
        result = result + self.reverseString(tmp)
        return result

    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        n = len(s)
        for i in range(int(n/2)):
            s[i], s[n-1-i] = s[n-1-i], s[i]
        return ''.join(s)
