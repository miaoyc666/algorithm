#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : jz-offer-28-dui-cheng-de-er-cha-shu.py
Author       : miaoyc
Create date  : 2022/3/3 11:53 PM
Description  : 对称的二叉树
"""

"""
难度：简单

与101 symmetric-tree题目重复

请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那么它是对称的。
例如，二叉树[1,2,2,3,4,4,3] 是对称的。
  1
 / \
 2  2
/ \ / \
3 4 4 3

但是下面这个[1,2,2,null,3,null,3] 则不是镜像对称的:
  1
 / \
 2  2
 \  \
 3  3

示例 1：
输入：root = [1,2,2,3,4,4,3]
输出：true

示例 2：
输入：root = [1,2,2,null,3,null,3]
输出：false

限制：
0 <= 节点个数 <= 1000
"""


class Solution(object):

    def check(self, left, right):
        """
        :type left: TreeNode
        :type right: TreeNode
        :rtype: bool
        """
        if not left and not right:
            return True
        if not left or not right:
            return False
        if left.val != right.val:
            return False
        return self.check(left.left, right.right) and self.check(left.right, right.left)

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.check(root, root)
