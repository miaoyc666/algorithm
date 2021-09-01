#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : _530_minimum-absolute-difference-in-bst.py
Author       : miaoyc
Create date  : 2021/7/7 12:15 上午
Description  : 二叉搜索树的最小绝对差
"""

"""
530. 二叉搜索树的最小绝对差
给你一棵所有节点为非负值的二叉搜索树，请你计算树中任意两节点的差的绝对值的最小值。

示例：

输入：

   1
    \
     3
    /
   2

输出：
1

解释：
最小绝对差为 1，其中 2 和 1 的差的绝对值为 1（或者 2 和 3）。
 

提示：
树中至少有 2 个节点。
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):

    def __init__(self):
        self.data = []
        self.min = None

    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.inorder(root)
        return self.min

    def diff(self):
        if len(self.data) == 1:
            return
        if not self.min:
            self.min = self.data[-1] - self.data[-2]
        elif self.data[-1] - self.data[-2] < self.min:
            self.min = self.data[-1] - self.data[-2]

    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        self.data.append(root.val)
        self.diff()
        self.inorder(root.right)
