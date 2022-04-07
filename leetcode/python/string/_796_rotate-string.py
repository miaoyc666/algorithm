#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : _796_rotate-string.py
Author       : miaoyc
Create date  : 2022/4/7 23:37
Description  : 旋转字符串
"""

"""
难度：简单

给定两个字符串, s和goal。如果在若干次旋转操作之后，s能变成goal，那么返回true。
s的 旋转操作 就是将s 最左边的字符移动到最右边。

例如, 若s = 'abcde'，在旋转一次之后结果就是'bcdea'。

示例 1:
输入: s = "abcde", goal = "cdeab"
输出: true

示例 2:
输入: s = "abcde", goal = "abced"
输出: false

提示:
1 <= s.length, goal.length <= 100
s和goal由小写英文字母组成
"""


class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return len(s) == len(goal) and goal in s + s
