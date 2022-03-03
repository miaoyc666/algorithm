#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : jz-offer-27-er-cha-shu-de-jing-xiang.py
Author       : miaoyc
Create date  : 2022/3/3 11:44 PM
Description  : 二叉树的镜像
"""

"""
难度：简单

与226 invert-binary-tree题目重复

请完成一个函数，输入一个二叉树，该函数输出它的镜像。

例如输入：
   4
  / \
  2  7
/  \ / \
1  3 6  9

镜像输出：
   4
  / \
  7  2
/ \ / \
9 6 3  1

示例 1：
输入：root = [4,2,7,1,3,6,9]
输出：[4,7,2,9,6,3,1]

限制：
0 <= 节点个数 <= 1000
"""


import copy


class Solution(object):

    def __init__(self):
        self.tmp = None

    def mirrorTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return

        self.mirrorTree(root.left)
        self.mirrorTree(root.right)

        self.tmp = root.left
        root.left = copy.deepcopy(root.right)
        root.right = copy.deepcopy(self.tmp)

        return root
