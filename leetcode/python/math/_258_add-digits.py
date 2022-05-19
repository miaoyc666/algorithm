#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : _258_add-digits.py
Author       : miaoyc
Create date  : 2022/3/3 9:57 PM 
Description  : 各位相加
"""

"""
难度：简单

给定一个非负整数 num，反复将各个位上的数字相加，直到结果为一位数。返回这个结果。

示例 1:
输入: num = 38
输出: 2 
解释: 各位相加的过程为：
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2
由于2 是一位数，所以返回 2。

示例 2:
输入: num = 0
输出: 0

提示：
0 <= num <= 231- 1
"""


"""
解题思路：

"""


class Solution:
    def addDigits(self, num: int) -> int:
        return (num - 1) % 9 + 1 if num else 0


# class Solution:
#     def addDigits(self, num: int) -> int:
#         queue = [num]
#         while len(queue) != 0:
#             c = 0
#             n = queue.pop()
#             if n < 10:
#                 return n
#             for i in str(n):
#                 c += int(i)
#             queue.append(c)
#
#
# class Solution:
#     def addDigits(self, num: int) -> int:
#         while num >= 10:
#             c = 0
#             for i in str(num):
#                 c += int(i)
#             num = c
#         return num
#