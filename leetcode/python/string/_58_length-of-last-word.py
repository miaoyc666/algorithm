#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : _58_length-of-last-word.py
Author       : miaoyc
Create date  : 2021/8/19 12:44 上午
Description  : 最后一个单词的长度
"""

"""
给你一个字符串 s，由若干单词组成，单词前后用一些空格字符隔开。返回字符串中最后一个单词的长度。

单词 是指仅由字母组成、不包含任何空格字符的最大子字符串。

示例 1：
输入：s = "Hello World"
输出：5
示例 2：

输入：s = "   fly me   to   the moon  "
输出：4
示例 3：

输入：s = "luffy is still joyboy"
输出：6

提示：
1 <= s.length <= 104
s 仅有英文字母和空格 ' ' 组成
s 中至少存在一个单词
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] != " ":
                count += 1
            if s[i] == " " and count != 0:
                return count
        return count
