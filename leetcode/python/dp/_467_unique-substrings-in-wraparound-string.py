#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : _467_unique-substrings-in-wraparound-string.py
Author       : miaoyc
Create date  : 2022/5/25 20:35 
Description  : 环绕字符串中唯一的子字符串
"""

"""
难度：中等

把字符串 s 看作是“abcdefghijklmnopqrstuvwxyz”的无限环绕字符串，所以s 看起来是这样的：
"...zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd....".
现在给定另一个字符串 p 。返回s 中唯一 的 p 的 非空子串的数量。

示例1:
输入: p = "a"
输出: 1
解释: 字符串 s 中只有一个"a"子字符。

示例 2:
输入: p = "cac"
输出: 2
解释: 字符串 s 中的字符串“cac”只有两个子串“a”、“c”。.

示例 3:
输入: p = "zab"
输出: 6
解释: 在字符串 s 中有六个子串“z”、“a”、“b”、“za”、“ab”、“zab”。

提示:
1 <= p.length <= 105
p由小写英文字母构成
"""

from collections import defaultdict


class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        dp = defaultdict(int)
        k = 0
        for i, ch in enumerate(p):
            # print(i, ch, ord(ch), p[i - 1], ord(p[i - 1]))
            # 字符之差为1表示连续的字符，原题目中s是连续的字符
            if i > 0 and (ord(ch) - ord(p[i - 1])) % 26 == 1:  # 字符之差为 1 或 -25
                k += 1
                print(1)
            else:
                print(2)
                k = 1
            dp[ch] = max(dp[ch], k)
        # print(dp)
        return sum(dp.values())
