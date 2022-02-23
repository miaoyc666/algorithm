#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : _917_reverse-only-letters.py
Author       : miaoyc
Create date  : 2022/2/23 10:06 PM 
Description  : 仅仅反转字母
"""

"""
难度：简单

给你一个字符串 s ，根据下述规则反转字符串：
所有非英文字母保留在原有位置。
所有英文字母（小写或大写）位置反转。
返回反转后的 s 。

示例 1：
输入：s = "ab-cd"
输出："dc-ba"
示例 2：

输入：s = "a-bC-dEf-ghIj"
输出："j-Ih-gfE-dCba"
示例 3：

输入：s = "Test1ng-Leet=code-Q!"
输出："Qedo1ct-eeLg=ntse-T!"

提示
1 <= s.length <= 100
s 仅由 ASCII 值在范围 [33, 122] 的字符组成
s 不含 '\"' 或 '\\'
"""


class Solution:

    def action(self, s):
        return s.isalpha()

    def reverseOnlyLetters(self, s: str) -> str:
        res = list(s)
        left, right = 0, len(res) - 1
        while left < right:
            l = self.action(res[left])
            r = self.action(res[right])
            while left < right and l and not r:
                right -= 1
                r = self.action(res[right])
            while left < right and not l and r:
                left += 1
                l = self.action(res[left])
            if l and r:
                res[left], res[right] = res[right], res[left]
                left += 1
                right -= 1
            if not l and not r:
                left += 1
                right -= 1
        return "".join(res)

