#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : jz-offer-48-zui-chang-bu-han-zhong-fu-zi-fu-de-zi-zi-fu-chuan.py
Author       : miaoyc
Create date  : 2022/3/3 11:58 PM
Description  : 最长不含重复字符的子字符串
"""

"""
难度：中等

与3 longest-substring-without-repeating-characters题目重复

请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。
示例1:
输入: "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

示例 2:
输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

示例 3:
输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是"wke"，所以其长度为 3。
    请注意，你的答案必须是 子串 的长度，"pwke"是一个子序列，不是子串。

提示：
s.length <= 40000
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        什么是滑动窗口？
        其实就是一个队列,比如例题中的 abcabcbb，进入这个队列（窗口）为 abc 满足题目要求，当再进入 a，队列变成了 abca，这时候不满足要求。所以，我们要移动这个队列！
        如何移动？
        我们只要把队列的左边的元素移出就行了，直到满足题目要求！
        一直维持这样的队列，找出队列出现最长的长度时候，求出解！
        时间复杂度：O(n)
        """
        if not s:
            return 0
        seen = set()
        cur_len, max_len, left = 0, 0, 0
        for i in range(len(s)):
            cur_len += 1
            # while循环为了找到第一个s[i]的位置，把s[i]之前的都移除
            while s[i] in seen:
                seen.remove(s[left])
                left += 1
                cur_len -= 1
            if cur_len > max_len:
                max_len = cur_len
            seen.add(s[i])
        return max_len
