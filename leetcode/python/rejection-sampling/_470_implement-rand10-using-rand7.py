#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : _470_implement-rand10-using-rand7.py
Author       : miaoyc
Create date  : 2022/6/11 00:09
Description  : 用Rand7()实现Rand10()
"""

"""
难度：中等

给定方法rand7可生成 [1,7] 范围内的均匀随机整数，试写一个方法rand10生成 [1,10] 范围内的均匀随机整数。
你只能调用rand7()且不能调用其他方法。请不要使用系统的Math.random()方法。
每个测试用例将有一个内部参数 n，即你实现的函数 rand10() 在测试时将被调用的次数。请注意，这不是传递给 rand10() 的参数。

示例 1:
输入: 1
输出: [2]

示例 2:
输入: 2
输出: [2,8]

示例 3:
输入: 3
输出: [3,8,10]

提示:
1 <= n <= 105

进阶:
rand7()调用次数的期望值是多少?
你能否尽量少调用 rand7() ?
"""


# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7
def rand7():
    pass


class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        while True:
            rand49 = (rand7() - 1) * 7 + rand7()
            if rand49 <= 40:
                return rand49 % 10 + 1
