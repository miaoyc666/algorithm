#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : _1108_defanging-an-ip-address.py
Author       : miaoyc
Create date  : 2022/6/22 22:55
Description  : IP地址无效化
"""

"""
难度：简单

给你一个有效的 IPv4 地址address，返回这个 IP 地址的无效化版本。
所谓无效化IP 地址，其实就是用"[.]"代替了每个 "."。

示例 1：
输入：address = "1.1.1.1"
输出："1[.]1[.]1[.]1"

示例 2：
输入：address = "255.100.50.0"
输出："255[.]100[.]50[.]0"

提示：
给出的address是一个有效的 IPv4 地址
"""


class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.', '[.]')
