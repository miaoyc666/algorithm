#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : _965_univalued-binary-tree.py
Author       : miaoyc
Create date  : 2021/11/10 11:49 下午
Description  : 单值二叉树
"""

"""
如果二叉树每个节点都具有相同的值，那么该二叉树就是单值二叉树。
只有给定的树是单值二叉树时，才返回true；否则返回 false。

示例 1：
输入：[1,1,1,1,1,null,1]
输出：true

示例 2：
输入：[2,2,2,5,2]
输出：false

提示：
给定树的节点数范围是[1, 100]。
每个节点的值都是整数，范围为[0, 99]。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.value = None

    def isUnivalTree(self, root: TreeNode) -> bool:
        self.value = root.val
        return self.inorder(root)

    def action(self, root):
        return True if root.val == self.value else False

    def inorder(self, root):
        if not root:
            return True
        if not self.inorder(root.left):
            return False
        if not self.action(root):
            return False
        if not self.inorder(root.right):
            return False
        return True
