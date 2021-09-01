#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : _interview_01.06_compress-string-lcci.py
Author       : miaoyc
Create date  : 2020/8/9 4:47 下午
Description  : 压缩字符串
"""

"""
字符串压缩。利用字符重复出现的次数，编写一种方法，实现基本的字符串压缩功能。
比如，字符串aabcccccaaa会变为a2b1c5a3。若“压缩”后的字符串没有变短，则返回原先的字符串。你可以假设字符串中只包含大小写英文字母（a至z）。

示例1:
输入："aabcccccaaa"
输出："a2b1c5a3"

示例2:
输入："abbccd"
输出："abbccd"
解释："abbccd"压缩后为"a1b2c2d1"，比原字符串长度更长。
提示：

字符串长度在[0, 50000]范围内。
"""


class Solution(object):
    def compressString(self, S):
        """
        :type S: str
        :rtype: str
        """
        if len(S) <= 2:
            return S
        head = S[0]
        v = head
        n = 1
        result = ""
        for i in S[1:]:
            if v == i:
                n += 1
            else:
                result += "{0}{1}".format(v, n)
                n = 1
                v = i
        result += "{0}{1}".format(v, n)
        if len(result) < len(S):
            return result
        else:
            return S
