#!/usr/bin/env python
# encoding:utf-8

"""
hihocoder题目描述
#1014 : Trie树
时间限制:10000ms
单点时限:1000ms
内存限制:256MB
描述
小Hi和小Ho是一对好朋友，出生在信息化社会的他们对编程产生了莫大的兴趣，他们约定好互相帮助，在编程的学习道路上一同前进。
这一天，他们遇到了一本词典，于是小Hi就向小Ho提出了那个经典的问题：
“小Ho，你能不能对于每一个我给出的字符串，都在这个词典里面找到以这个字符串开头的所有单词呢？”
身经百战的小Ho答道：
“怎么会不能呢！你每给我一个字符串，我就依次遍历词典里的所有单词，检查你给我的字符串是不是这个单词的前缀不就是了？”
小Hi笑道：“你啊，还是太年轻了！~假设这本词典里有10万个单词，我询问你一万次，你得要算到哪年哪月去？”
小Ho低头算了一算，看着那一堆堆的0，顿时感觉自己这辈子都要花在上面了...
小Hi看着小Ho的囧样，也是继续笑道：“让我来提高一下你的知识水平吧~你知道树这样一种数据结构么？”
小Ho想了想，说道：“知道~它是一种基础的数据结构，就像这里说的一样！”
小Hi满意的点了点头，说道：“那你知道我怎么样用一棵树来表示整个词典么？”
小Ho摇摇头表示自己不清楚。

提示一：Trie树的建立
“你看，我们现在得到了这样一棵树，那么你看，如果我给你一个字符串ap，你要怎么找到所有以ap开头的单词呢？”小Hi又考校小Ho。
“唔...一个个遍历所有的单词？”小Ho还是不忘自己最开始提出来的算法。
“笨！这棵树难道就白构建了！”小Hi教训完小Ho，继续道：“看好了！”

提示二：如何使用Trie树
提示三：在建立Trie树时同时进行统计！

“那么现在！赶紧去用代码实现吧！”小Hi如是说道

输入
输入的第一行为一个正整数n，表示词典的大小，其后n行，每一行一个单词（不保证是英文单词，也有可能是火星文单词哦），
单词由不超过10个的小写英文字母组成，可能存在相同的单词，此时应将其视作不同的单词。
接下来的一行为一个正整数m，表示小Hi询问的次数，其后m行，
每一行一个字符串，该字符串由不超过10个的小写英文字母组成，表示小Hi的一个询问。

在20%的数据中n, m<=10，词典的字母表大小<=2.
在60%的数据中n, m<=1000，词典的字母表大小<=5.
在100%的数据中n, m<=100000，词典的字母表大小<=26.

本题按通过的数据量排名哦～

输出
对于小Hi的每一个询问，输出一个整数Ans,表示词典中以小Hi给出的字符串为前缀的单词的个数。

样例输入
5
babaab
babbbaaaa
abba
aaaaabaa
babaababb
5
babb
baabaaa
bab
bb
bbabbaab
样例输出
1
0
3
0
0
"""

from collections import defaultdict


class TrieNode(object):
    """
    前缀树节点
    """
    def __init__(self):
        self.nodes = defaultdict(TrieNode)
        self.count = 1


class Trie(object):
    """
    前缀树
    """

    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        """
        新增节点
        :param word:
        :return:
        """
        cur = self.root
        for char in word:
            if char in cur.nodes:
                cur.nodes[char].count += 1
            cur = cur.nodes[char]

    def find(self, prefix):
        """
        查找节点
        :param prefix:
        :return:
        """
        cur = self.root
        for char in prefix:
            if char not in cur.nodes:
                return 0
            cur = cur.nodes[char]
        return cur.count
