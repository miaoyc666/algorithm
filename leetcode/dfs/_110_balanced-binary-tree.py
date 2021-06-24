#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : _110_balanced-binary-tree.py
Author       : miaoyc
Create date  : 2021/6/24 3:36 下午
Description  : 平衡二叉树
"""

"""
给定一个二叉树，判断它是否是高度平衡的二叉树。
本题中，一棵高度平衡二叉树定义为：
一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1 。

示例 1：

输入：root = [3,9,20,null,null,15,7]
输出：true
示例 2：

输入：root = [1,2,2,3,3,null,null,4,4]
输出：false
示例 3：

输入：root = []
输出：true

提示：

树中的节点数在范围 [0, 5000] 内
-104 <= Node.val <= 104
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):

    def height(self, root):
        # check root null
        if not root:
            return 0

        # check left
        left = self.height(root.left)
        if left == -1:
            return -1

        # check right
        right = self.height(root.right)
        if right == -1:
            return -1

        # diff
        return max(left, right) + 1 if abs(left - right) < 2 else -1

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.height(root) != -1
