#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : _111_minimum-depth-of-binary-tree.py
Author       : miaoyc
Create date  : 2021/6/25 2:29 上午
Description  : 二叉树的最小深度
"""

"""
给定一个二叉树，找出其最小深度。

最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

说明：叶子节点是指没有子节点的节点。

示例 1：

输入：root = [3,9,20,null,null,15,7]
输出：2
示例 2：

输入：root = [2,null,3,null,4,null,5,null,6]
输出：5

提示：

树中节点数的范围在 [0, 105] 内
-1000 <= Node.val <= 1000
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        left = self.minDepth(root.left)
        right = self.minDepth(root.right)

        return left + right + 1 if left == 0 or right == 0 else min(left, right) + 1
