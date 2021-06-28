#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : _144_binary-tree-preorder-traversal.py
Author       : miaoyc
Create date  : 2021/6/28 11:11 下午
Description  : 二叉树的前序遍历
"""

"""
给你二叉树的根节点 root ，返回它节点值的 前序 遍历。

 

示例 1：


输入：root = [1,null,2,3]
输出：[1,2,3]
示例 2：

输入：root = []
输出：[]
示例 3：

输入：root = [1]
输出：[1]
示例 4：


输入：root = [1,2]
输出：[1,2]
示例 5：


输入：root = [1,null,2]
输出：[1,2]

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):

    def __init__(self):
        self.result = []

    def pre(self, root):
        if not root:
            return
        self.result.append(root.val)
        self.pre(root.left)
        self.pre(root.right)

    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.pre(root)
        return self.result
