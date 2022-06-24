#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : _515_find-largest-value-in-each-tree-row.py
Author       : miaoyc
Create date  : 2022/6/24 22:09 
Description  : 在每个树行中找最大值
"""

"""
难度：中等

给定一棵二叉树的根节点root ，请找出该二叉树中每一层的最大值。

示例1：
输入: root = [1,3,2,5,3,null,9]
输出: [1,3,9]

示例2：
输入: root = [1,2,3]
输出: [1,3]

提示：
二叉树的节点个数的范围是 [0,104]
-231<= Node.val <= 231- 1
"""

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        q, res = [root], []
        while len(q) > 0:
            size = len(q)
            m =
            for i in range(size):
                head = q.pop(0)
                if head.left:
                    q.append(head.left)
                if head.right:
                    q.append(head.right)
                