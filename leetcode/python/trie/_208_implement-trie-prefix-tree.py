#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : _208_implement-trie-prefix-tree.py
Author       : miaoyc
Create date  : 2022/3/17 11:36 PM 
Description  : 实现 Trie (前缀树)
"""

"""
难度：中等

Trie（发音类似 "try"）或者说 前缀树 是一种树形数据结构，用于高效地存储和检索字符串数据集中的键。这一数据结构有相当多的应用情景，例如自动补完和拼写检查。
请你实现 Trie 类：
Trie() 初始化前缀树对象。
void insert(String word) 向前缀树中插入字符串 word 。
boolean search(String word) 如果字符串 word 在前缀树中，返回 true（即，在检索之前已经插入）；否则，返回 false 。
boolean startsWith(String prefix) 如果之前已经插入的字符串word 的前缀之一为 prefix ，返回 true ；否则，返回 false 。

示例：
输入
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]

输出
[null, null, true, false, true, null, true]

解释
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // 返回 True
trie.search("app");     // 返回 False
trie.startsWith("app"); // 返回 True
trie.insert("app");
trie.search("app");     // 返回 True

提示：
1 <= word.length, prefix.length <= 2000
word 和 prefix 仅由小写英文字母组成
insert、search 和 startsWith 调用次数 总计 不超过 3 * 104 次
"""


from collections import defaultdict


class TrieNode(object):
    """
    前缀树节点
    """
    def __init__(self):
        self.nodes = defaultdict(TrieNode)
        self.count = 1
        self.is_world = None


class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        新增节点
        :param word:
        :return:
        """
        cur = self.root
        for char in word:
            if char not in cur.nodes:
                cur.nodes[char].count += 1
            cur = cur.nodes[char]
        cur.is_world = True

    def search_prefix(self, word: str) -> TrieNode:
        """
        查找前缀
        :param word:
        :return:
        """
        cur = self.root
        for char in word:
            if char not in cur.nodes:
                return None
            cur = cur.nodes[char]
        return cur

    def search(self, word: str) -> bool:
        """
        查找节点
        :param word:
        :return:
        """
        cur = self.search_prefix(word)
        return True if cur and cur.is_world else False

    def startsWith(self, prefix: str) -> bool:
        """
        前缀
        :param word:
        :return:
        """
        cur = self.search_prefix(prefix)

        return True if cur else False


obj = Trie()
obj.insert("apple")
param_2 = obj.search("apple")
param_3 = obj.search("app")
# param_3 = obj.startsWith(prefix)

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
