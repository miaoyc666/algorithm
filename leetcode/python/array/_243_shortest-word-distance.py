#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : _243_shortest-word-distance.py
Author       : miaoyc
Create date  : 2022/5/27 21:59 
Description  : 最短单词距离
"""

"""
难度：简单

给定一个字符串数组wordDict和两个已经存在于该数组中的不同的字符串word1 和 word2 。返回列表中这两个单词之间的最短距离。

示例 1:
输入: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "coding", word2 = "practice"
输出: 3

示例2:
输入: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "coding"
输出: 1

提示:
1 <= wordsDict.length <= 3 * 104
1 <= wordsDict[i].length <= 10
wordsDict[i]由小写英文字母组成
word1和word2在wordsDict 中
word1 != word2
"""

from typing import List


class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        r = len(wordsDict)
        i1, i2 = -1, -1
        for i, w in enumerate(wordsDict):
            if w == word1:
                i1 = i
            if w == word2:
                i2 = i
            if i1 >= 0 and i2 >= 0:
                r = min(r, abs(i1-i2))
        return r