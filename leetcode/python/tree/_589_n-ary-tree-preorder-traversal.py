#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : _589_n-ary-tree-preorder-traversal.py
Author       : miaoyc
Create date  : 2022/3/10 11:01 PM 
Description  : N 叉树的前序遍历
"""

"""
难度：简单

给定一个n叉树的根节点root，返回其节点值的前序遍历 。

n叉树在输入中按层序遍历进行序列化表示，每组子节点由空值null分隔（请参见示例）。

示例 1：
输入：root = [1,null,3,2,4,null,5,6]
输出：[1,3,5,6,2,4]

示例 2：
输入：root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
输出：[1,2,3,6,7,11,14,4,8,12,5,9,13,10]

提示：
节点总数在范围[0, 104]内
0 <= Node.val <= 104
n 叉树的高度小于或等于 1000
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

from typing import List


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        self.dfs(root)
        return self.res

    def __init__(self):
        self.res = []

    def dfs(self, root):
        if not root:
            return
        self.res.append(root.val)
        for i in root.children:
            self.dfs(i)
