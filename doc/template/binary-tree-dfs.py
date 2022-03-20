#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : binary-tree-dfs.py
Author       : miaoyc
Create date  : 2021/11/11 12:36 上午
Description  : 二叉树问题处理模板
"""

"""
此模板为递归处理模板
二叉树遍历问题，首先要找到递归处理的退出条件，其次找到遍历顺序和对节点的处理
经典的二叉树前中后序三种遍历
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def action(self, root):
        # 对节点的处理，此处打印仅为举例
        print(root.val)

    def preorder(self, root):
        """
        前序遍历
        :param root:
        :return:
        """
        if not root:
            return
        self.result.append(root.val)
        self.preorder(root.left)
        self.preorder(root.right)

    def inorder(self, root):
        """
        中序遍历
        :param root:
        :return:
        """
        # 退出条件，此处root节点不存在仅为举例
        if not root:
            return
        self.inorder(root.left)
        self.action(root)
        self.inorder(root.right)

    def postorder(self, root):
        """
        后序遍历
        :param root:
        :return:
        """
        if not root:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        self.result.append(root.val)


