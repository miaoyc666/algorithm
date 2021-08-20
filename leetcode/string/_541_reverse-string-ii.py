#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : _541_reverse-string-ii.py
Author       : miaoyc
Create date  : 2021/8/20 11:54 下午
Description  : 反转字符串 II
"""

"""
给定一个字符串 s 和一个整数 k，从字符串开头算起，每 2k 个字符反转前 k 个字符。
如果剩余字符少于 k 个，则将剩余字符全部反转。
如果剩余字符小于 2k 但大于或等于 k 个，则反转前 k 个字符，其余字符保持原样。

示例 1：

输入：s = "abcdefg", k = 2
输出："bacdfeg"
示例 2：

输入：s = "abcd", k = 2
输出："bacd"

提示：
1 <= s.length <= 104
s 仅由小写英文组成
1 <= k <= 104
"""
