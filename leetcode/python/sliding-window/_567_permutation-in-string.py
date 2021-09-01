#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : _567_permutation-in-string.py
Author       : miaoyc
Create date  : 2021/7/27 0:20
Description  : 字符串的排列
"""

"""
给定两个字符串s1和s2，写一个函数来判断 s2 是否包含 s1的排列。

换句话说，第一个字符串的排列之一是第二个字符串的 子串 。



示例 1：

输入: s1 = "ab" s2 = "eidbaooo"
输出: True
解释: s2 包含 s1 的排列之一 ("ba").
示例 2：

输入: s1= "ab" s2 = "eidboaoo"
输出: False


提示：

1 <= s1.length, s2.length <= 104
s1 和 s2 仅包含小写字母
通过次数97,559提交次数228,358
"""


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # 我们定义 counter1 是对 s1 内字符出现的个数的统计，定义 counter2 是对 s2 内字符出现的个数的统计。
        # 初始化counter1
        counter1 = {}
        for i in s1:
            if i not in counter1:
                counter1[i] = 0
            counter1[i] += 1

        # 初始化游标
        left = 0
        right = len(s1) - 1
        # 初始化counter2
        counter2 = {}
        for i in s2[left: right]:
            if i not in counter2:
                counter2[i] = 0
            counter2[i] += 1
        #
        while right < len(s2):
            if s2[right] not in counter2:
                counter2[s2[right]] = 0
            counter2[s2[right]] += 1
            # 比较是否相同
            if counter1 == counter2:
                return True
            # left游标所指向的字符计数减1
            counter2[s2[left]] -= 1
            if counter2[s2[left]] == 0:
                del counter2[s2[left]]
            left += 1
            right += 1

        return False





