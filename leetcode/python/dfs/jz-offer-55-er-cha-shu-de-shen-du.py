#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : jz-offer-55-er-cha-shu-de-shen-du.py
Author       : miaoyc
Create date  : 2022/1/19 11:47 下午
Description  : 二叉树的深度
"""

"""
难度：简单

与104 maximum-depth-of-binary-tree题目重复
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        return self.dfs(root)

    def dfs(self, root):
        # 退出条件，此处root节点不存在仅为举例
        if not root:
            return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        return left + 1 if left > right else right + 1
