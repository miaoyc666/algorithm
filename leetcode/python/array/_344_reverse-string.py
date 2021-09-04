#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : _344_reverse-string.py
Author       : miaoyc
Create date  : 2021/7/22 2:53 上午
Description  : 反转字符串
"""

"""
编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 char[] 的形式给出。

不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。

你可以假设数组中的所有字符都是 ASCII 码表中的可打印字符。



示例 1：

输入：["h","e","l","l","o"]
输出：["o","l","l","e","h"]
示例 2：

输入：["H","a","n","n","a","h"]
输出：["h","a","n","n","a","H"]
"""


class Solution(object):

    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        n = len(s)
        for i in range(int(n/2)):
            s[i], s[n-1-i] = s[n-1-i], s[i]
