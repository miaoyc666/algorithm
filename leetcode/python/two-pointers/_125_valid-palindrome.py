#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : _125_valid-palindrome.py
Author       : miaoyc
Create date  : 2021/9/30 11:48 下午
Description  : 验证回文串
"""

"""
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
说明：本题中，我们将空字符串定义为有效的回文串。

示例 1:
输入: "A man, a plan, a canal: Panama"
输出: true
解释："amanaplanacanalpanama" 是回文串

示例 2:
输入: "race a car"
输出: false
解释："raceacar" 不是回文串

提示：
1 <= s.length <= 2 * 105
字符串 s 由 ASCII 字符组成
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        left, right = 0, n - 1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if left < right:
                if s[left].lower() != s[right].lower():
                    return False
                left, right = left + 1, right - 1
        return True
