#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : _14_longest-common-prefix.py
Author       : miaoyc
Create date  : 2021/8/4 11:55 下午
Description  : 最长公共前缀
"""

from typing import List

"""
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串""。

示例 1：

输入：strs = ["flower","flow","flight"]
输出："fl"
示例 2：

输入：strs = ["dog","racecar","car"]
输出：""
解释：输入不存在公共前缀。

提示：

0 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] 仅由小写英文字母组成
"""


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]
        # 把输入的数组转换为矩阵处理，纵向比较
        index = self.find(strs)
        if index is not None:
            return strs[0][:index+1]
        else:
            return ""

    def find_length(self, strs):
        return max([len(i) for i in strs])

    def find(self, strs):
        if not strs:
            return None
        eq = None
        tmp = strs[0]
        for i in range(self.find_length(strs)):
            if not strs[0]:
                return None
            for st in strs:
                if i >= len(st) or st[i] != tmp[i]:
                    return i-1 if eq else None
            eq = True
        return len(strs[0])-1
