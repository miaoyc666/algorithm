#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : _102_binary-tree-level-order-traversal.py
Author       : miaoyc
Create date  : 2022/1/15 12:46 下午
Description  : 二叉树层序遍历
"""

"""
难度：中等

给你二叉树的根节点 root ，返回其节点值的 层序遍历 。 （即逐层地，从左到右访问所有节点）。

示例 1：
输入：root = [3,9,20,null,null,15,7]
输出：[[3],[9,20],[15,7]]

示例 2：
输入：root = [1]
输出：[[1]]

示例 3：
输入：root = []
输出：[]

提示：
树中节点数目在范围 [0, 2000] 内
-1000 <= Node.val <= 1000
"""

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    def __init__(self):
        self.queue_ = []
        self.result = []

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        self.queue_ = [root]
        self.result.append([root.val])
        while len(self.queue_) > 0:
            size = len(self.queue_)
            layer = []
            for i in range(size):
                head = self.queue_.pop(0)
                if head.left:
                    layer.append(head.left.val)
                    self.queue_.append(head.left)
                if head.right:
                    layer.append(head.right.val)
                    self.queue_.append(head.right)
            if layer:
                self.result.append(layer)
        return self.result
