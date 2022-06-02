#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : _450_delete-node-in-a-bst.py
Author       : miaoyc
Create date  : 2022/6/3 00:00
Description  : 
"""

"""
难度：中等

给定一个二叉搜索树的根节点 root 和一个值 key，删除二叉搜索树中的key对应的节点，并保证二叉搜索树的性质不变。返回二叉搜索树（有可能被更新）的根节点的引用。
一般来说，删除节点可分为两个步骤：
首先找到需要删除的节点；
如果找到了，删除它。

示例 1:
输入：root = [5,3,6,2,4,null,7], key = 3
输出：[5,4,6,2,null,null,7]
解释：给定需要删除的节点值是 3，所以我们首先找到 3 这个节点，然后删除它。
一个正确的答案是 [5,4,6,2,null,null,7], 如下图所示。
另一个正确答案是 [5,2,6,null,4,null,7]。

示例 2:
输入: root = [5,3,6,2,4,null,7], key = 0
输出: [5,3,6,2,4,null,7]
解释: 二叉树不包含值为 0 的节点

示例 3:
输入: root = [], key = 0
输出: []

提示:

节点数的范围[0, 104].
-105<= Node.val <= 105
节点值唯一
root是合法的二叉搜索树
-105<= key <= 105

进阶： 要求算法时间复杂度为O(h)，h 为树的高度。
"""

"""
解题思路

当前节点比删除值小，右子树的根变为右子树中删除；
当前节点比删除值大，左子树的根变为左子树中删除；
当前就是要被删的节点，如果它没有左子树或没有右子树，可以直接平移嫁接。
否则需要找到左子树最大值或右子树最小值作为新的根。
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if root:
            if root.val < key:
                root.right = self.deleteNode(root.right, key)
            elif root.val > key:
                root.left = self.deleteNode(root.left, key)
            else:
                if not root.left or not root.right:
                    root = root.left if root.left else root.right
                else:
                    node = root.left
                    while node.right:
                        node = node.right
                    node.left = self.deleteNode(root.left, node.val)
                    node.right = root.right
                    root = node
        return root

