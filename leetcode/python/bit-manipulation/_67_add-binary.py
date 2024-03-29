#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : _67_add-binary.py
Author       : miaoyc
Create date  : 2021/8/16 11:56 下午
Description  : 二进制求和
"""

"""
给你两个二进制字符串，返回它们的和（用二进制表示）。
输入为 非空 字符串且只包含数字1和0。

示例1:
输入: a = "11", b = "1"
输出: "100"

示例2:
输入: a = "1010", b = "1011"
输出: "10101"

提示：
每个字符串仅由字符 '0' 或 '1' 组成。
1 <= a.length, b.length <= 10^4
字符串如果不是 "0" ，就都不含前导零。
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = int(a, 2)
        b = int(b, 2)
        while b:
            result = a ^ b
            carry = (a & b) << 1
            # a & b << 1 表示进位
            a, b = result, carry
        return bin(a)[2:]
