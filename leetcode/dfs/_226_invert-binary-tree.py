#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : _226_invert-binary-tree.py
Author       : miaoyc
Create date  : 2021/6/29 10:58 上午
Description  : 翻转二叉树
"""

"""
翻转一棵二叉树。

示例：

输入：

     4
   /   \
  2     7
 / \   / \
1   3 6   9
输出：

     4
   /   \
  7     2
 / \   / \
9   6 3   1
备注:
这个问题是受到 Max Howell 的 原问题 启发的 ：

谷歌：我们90％的工程师使用您编写的软件(Homebrew)，但是您却无法在面试时在白板上写出翻转二叉树这道题，这太糟糕了。
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import copy


class Solution(object):

    def __init__(self):
        self.tmp = None

    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return

        self.invertTree(root.left)
        self.invertTree(root.right)

        self.tmp = root.left
        root.left = copy.deepcopy(root.right)
        root.right = copy.deepcopy(self.tmp)

        return root
