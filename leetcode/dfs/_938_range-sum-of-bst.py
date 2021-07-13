#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : _938_range-sum-of-bst.py
Author       : miaoyc
Create date  : 2021/7/13 11:51 下午
Description  : 二叉搜索树的范围和
"""

"""
给定二叉搜索树的根结点 root，返回值位于范围 [low, high] 之间的所有结点的值的和。

 

示例 1：


输入：root = [10,5,15,3,7,null,18], low = 7, high = 15
输出：32
示例 2：


输入：root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
输出：23
 

提示：

树中节点数目在范围 [1, 2 * 104] 内
1 <= Node.val <= 105
1 <= low <= high <= 105
所有 Node.val 互不相同

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):

    def __init__(self):
        self.sum = 0

    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        self.inorder(root, low, high)
        return self.sum

    def inorder(self, root, low, high):
        if not root:
            return
        self.inorder(root.left, low, high)
        if low <= root.val <= high:
            self.sum += root.val
        self.inorder(root.right, low, high)
