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
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):

    def __init__(self):
        self.queue_ = []

    def bfs(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        self.queue_ = [root]
        while len(self.queue_) > 0:
            size = len(self.queue_)
            for i in range(size):
                head = self.queue_.pop(0)
                if head.left:
                    self.queue_.append(head.left)
                if head.right:
                    self.queue_.append(head.right)
        return self.queue_
