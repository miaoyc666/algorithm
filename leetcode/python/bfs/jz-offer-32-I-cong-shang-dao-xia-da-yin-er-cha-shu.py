#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : jz-offer-32-I-cong-shang-dao-xia-da-yin-er-cha-shu.py
Author       : miaoyc
Create date  : 2022/1/15 12:46 下午
Description  : 从上到下打印二叉树
"""

"""
难度：中等

从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印。

例如:
给定二叉树:[3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
返回：
[3,9,20,15,7]

提示：
节点总数 <= 1000
"""
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def __init__(self):
        self.queue_ = []
        self.result = []

    def levelOrder(self, root: TreeNode) -> List[int]:
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        self.queue_ = [root]
        self.result.append(root.val)
        while len(self.queue_) > 0:
            size = len(self.queue_)
            for i in range(size):
                head = self.queue_.pop(0)
                if head.left:
                    self.queue_.append(head.left)
                    self.result.append(head.left.val)
                if head.right:
                    self.queue_.append(head.right)
                    self.result.append(head.right.val)
        return self.result
