#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : _404_sum-of-left-leaves.py
Author       : miaoyc
Create date  : 2021/7/3 11:43 下午
Description  : 左叶子之和
"""

"""
计算给定二叉树的所有左叶子之和。

示例：

    3
   / \
  9  20
    /  \
   15   7

在这个二叉树中，有两个左叶子，分别是 9 和 15，所以返回 24
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):

    def __init__(self):
        self.sum = 0

    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.dfs(0, root)
        return self.sum

    def dfs(self, sign, root):
        if not root:
            return
        if sign == 1 and not root.left and not root.right:
            self.sum += root.val

        self.dfs(1, root.left)
        self.dfs(0, root.right)
