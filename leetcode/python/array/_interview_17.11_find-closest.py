#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : _interview_17.11_find-closest.py
Author       : miaoyc
Create date  : 2022/5/27 21:29 
Description  : 单词距离
"""

"""
难度：中等
tag: array, string
与243 shortest-word-distance题目重复

有个内含单词的超大文本文件，给定任意两个不同的单词，找出在这个文件中这两个单词的最短距离(相隔单词数)。如果寻找过程在这个文件中会重复多次，而每次寻找的单词不同，你能对此优化吗?

示例：
输入：words = ["I","am","a","student","from","a","university","in","a","city"], word1 = "a", word2 = "student"
输出：1

提示：
words.length <= 100000
"""

from typing import List


class Solution:
    def findClosest(self, words: List[str], word1: str, word2: str) -> int:
        r = len(words)
        i1, i2 = -1, -1
        for i, w in enumerate(words):
            if w == word1:
                i1 = i
            if w == word2:
                i2 = i
            if i1 >= 0 and i2 >= 0:
                r = min(r, abs(i1-i2))
        return r
