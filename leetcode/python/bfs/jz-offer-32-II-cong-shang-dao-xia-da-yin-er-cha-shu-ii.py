#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : jz-offer-32-II-cong-shang-dao-xia-da-yin-er-cha-shu-ii.py
Author       : miaoyc
Create date  : 2022/2/28 11:05 PM 
Description  : 从上到下打印二叉树II
"""

"""
难度：中等

与102 binary-tree-level-order-traversal题目重复

从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。

例如:
给定二叉树:[3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [9,20],
  [15,7]
]

提示：
节点总数 <= 1000
"""

from typing import List


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.queue_ = []
        self.result = []

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        """
        :param root: TreeNode
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
