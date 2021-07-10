#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : _572_subtree-of-another-tree.py
Author       : miaoyc
Create date  : 2021/7/10 10:48 下午
Description  : 另一个树的子树
"""

"""
给定两个非空二叉树 s 和 t，检验 s 中是否包含和 t 具有相同结构和节点值的子树。s 的一个子树包括 s 的一个节点和这个节点的所有子孙。s 也可以看做它自身的一棵子树。

示例 1:
给定的树 s:

     3
    / \
   4   5
  / \
 1   2
给定的树 t：

   4 
  / \
 1   2
返回 true，因为 t 与 s 的一个子树拥有相同的结构和节点值。

示例 2:
给定的树 s：

     3
    / \
   4   5
  / \
 1   2
    /
   0
给定的树 t：

   4
  / \
 1   2
返回 false。
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 一个树是另一个树的子树 则

# 要么这两个树相等
# 要么这个树是左树的子树
# 要么这个树hi右树的子树


class Solution(object):

    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        if not root and not subRoot:
            return True
        if not root and subRoot:
            return False
        if root and not subRoot:
            return False
        return self.is_same_tree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def is_same_tree(self, root, target):
        if not root and not target:
            return True
        return root and target and root.val == target.val and self.is_same_tree(root.left, target.left) and self.is_same_tree(root.right, target.right)