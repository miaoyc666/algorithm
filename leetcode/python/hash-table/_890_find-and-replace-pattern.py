#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : _890_find-and-replace-pattern.py
Author       : miaoyc
Create date  : 2022/6/12 16:55
Description  : 查找和替换模式
"""

"""
难度：中等

你有一个单词列表words和一个模式pattern，你想知道 words 中的哪些单词与模式匹配。
如果存在字母的排列 p，使得将模式中的每个字母 x 替换为 p(x) 之后，我们就得到了所需的单词，那么单词与模式是匹配的。
（回想一下，字母的排列是从字母到字母的双射：每个字母映射到另一个字母，没有两个字母映射到同一个字母。）
返回 words 中与给定模式匹配的单词列表。
你可以按任何顺序返回答案。

示例：
输入：words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
输出：["mee","aqq"]
解释：
"mee" 与模式匹配，因为存在排列 {a -> m, b -> e, ...}。
"ccc" 与模式不匹配，因为 {a -> c, b -> c, ...} 不是排列。
因为 a 和 b 映射到同一个字母。

提示：
1 <= words.length <= 50
1 <= pattern.length = words[i].length<= 20
"""

from typing import List


class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def filter_w(w, p):
            if len(w) != len(p):
                return False
            return len(set(w)) == len(set(p)) == len(set(zip(w, p)))

        return [w for w in words if filter_w(w, pattern)]
