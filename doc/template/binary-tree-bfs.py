#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : binary-tree-bfs.py
Author       : miaoyc
Create date  : 2022/01/15 12:56 上午
Description  : 二叉树问题层序遍历模板
"""

"""
二叉树层序遍历问题
"""

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    def bfs(self, root):
        """
        :param root: TreeNode
        :rtype: List[TreeNode]
        """
        queue_ = [root]
        while len(queue_) > 0:
            size = len(queue_)
            for i in range(size):
                head = queue_.pop(0)
                if head.left:
                    queue_.append(head.left)
                if head.right:
                    queue_.append(head.right)
