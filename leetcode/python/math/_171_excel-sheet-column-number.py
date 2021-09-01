#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : _171_excel-sheet-column-number.py
Author       : miaoyc
Create date  : 2021/7/30 11:44 下午
Description  :  Excel 表列序号
"""

"""
给你一个字符串columnTitle ，表示 Excel 表格中的列名称。返回该列名称对应的列序号。

例如，

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...

示例 1:

输入: columnTitle = "A"
输出: 1
示例2:

输入: columnTitle = "AB"
输出: 28
示例3:

输入: columnTitle = "ZY"
输出: 701
示例 4:

输入: columnTitle = "FXSHRXW"
输出: 2147483647

提示：

1 <= columnTitle.length <= 7
columnTitle 仅由大写英文组成
columnTitle 在范围 ["A", "FXSHRXW"] 内
"""


class Solution:

    # 26进制转换解法，或者利用ascii码解法
    def titleToNumber(self, columnTitle: str) -> int:
        sums = 0
        for i in columnTitle:
            sums *= 26
            sums += ord(i) - ord("A") + 1
        return sums
