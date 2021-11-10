#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : dfs.py
Author       : miaoyc
Create date  : 2021/11/11 12:36 上午
Description  : 深度游先搜索模板，本质上就是一个二叉树的中序遍历
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

    def inorder(self, root):
        # 退出条件，此处root节点不存在仅为举例
        if not root:
            return
        self.inorder(self, root.left)
        self.action()
        self.inorder(self, root.right)

