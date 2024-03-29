#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : _28_implement-strstr.py
Author       : miaoyc
Create date  : 2021/8/15 5:20 下午
Description  : 实现 strStr()
"""

"""
实现strStr()函数。

给你两个字符串haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串出现的第一个位置（下标从 0 开始）。如果不存在，则返回 -1 。
说明：
当needle是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。
对于本题而言，当needle是空字符串时我们应当返回 0 。这与 C 语言的strstr()以及 Java 的indexOf()定义相符。

示例 1：
输入：haystack = "hello", needle = "ll"
输出：2

示例 2：
输入：haystack = "aaaaa", needle = "bba"
输出：-1

示例 3：
输入：haystack = "", needle = ""
输出：0

提示：
0 <= haystack.length, needle.length <= 5 * 104
haystack 和 needle 仅由小写英文字符组成
"""

"""
2022.4.7: 这tm写的是啥啊？我怎么一句都看不懂，字符串匹配最难的kmp应该是困难，怎么是简单？
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m, n = len(haystack), len(needle)
        if haystack == needle or not n:
            return 0
        if n > m:
            return -1
        total = int((m-n+1))
        for i in range(0, total):
            flag = self.match(haystack[i: i+n], needle)
            if flag:
                return i
        return -1

    def match(self, a, b):
        len_ = len(b)
        for i in range(0, len_):
            if a[i] == b[i] and a[len_-1-i] == b[len_-1-i]:
                continue
            else:
                return False
        return True
