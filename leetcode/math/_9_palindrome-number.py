#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : _9_palindrome-number.py
Author       : miaoyc
Create date  : 2021/7/1 11:44 下午
Description  : 回文数
"""

"""
给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。

回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。例如，121 是回文，而 123 不是。

 

示例 1：

输入：x = 121
输出：true
示例 2：

输入：x = -121
输出：false
解释：从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
示例 3：

输入：x = 10
输出：false
解释：从右向左读, 为 01 。因此它不是一个回文数。
示例 4：

输入：x = -101
输出：false
 

提示：

-231 <= x <= 231 - 1
 

进阶：你能不将整数转为字符串来解决这个问题吗？
"""


class Solution(object):

    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        if x % 10 == 0 and x != 0:
            return False

        revert_num = 0
        while x > revert_num:
            revert_num = revert_num * 10 + x % 10
            x /= 10

        return x == revert_num or x == revert_num / 10;

