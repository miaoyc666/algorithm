#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : _3_longest-substring-without-repeating-characters.py
Author       : miaoyc
Create date  : 2021/7/24 23:52
Description  : 无重复字符的最长子串
"""

"""
给定一个字符串 s ，请你找出其中不含有重复字符的最长子串的长度。

示例1:

输入: s = "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是"wke"，所以其长度为 3。
    请注意，你的答案必须是 子串 的长度，"pwke"是一个子序列，不是子串。
示例 4:

输入: s = ""
输出: 0

提示：

0 <= s.length <= 5 * 104
s由英文字母、数字、符号和空格组成
"""

