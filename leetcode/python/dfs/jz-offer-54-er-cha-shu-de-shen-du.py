#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : jz-offer-54-er-cha-shu-de-shen-du.py
Author       : miaoyc
Create date  : 2022/1/19 11:47 下午
Description  : 二叉树的深度
"""

"""
难度：简单

输入一棵二叉树的根节点，求该树的深度。从根节点到叶节点依次经过的节点（含根、叶节点）形成树的一条路径，最长路径的长度为树的深度。

例如：
给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度3 。

提示：
节点总数 <= 10000
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
