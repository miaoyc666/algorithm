#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : _94_binary-tree-inorder-traversal.py
Author       : miaoyc
Create date  : 2021/6/28 11:16 下午
Description  : 二叉树的中序遍历
"""

"""
给定一个二叉树的根节点 root ，返回它的 中序 遍历。

 

示例 1：

输入：root = [1,null,2,3]
输出：[1,3,2]
示例 2：

输入：root = []
输出：[]
示例 3：

输入：root = [1]
输出：[1]
示例 4：


输入：root = [1,2]
输出：[2,1]
示例 5：


输入：root = [1,null,2]
输出：[1,2]
 

提示：

树中节点数目在范围 [0, 100] 内
-100 <= Node.val <= 100
 

进阶: 递归算法很简单，你可以通过迭代算法完成吗？

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):

    def __init__(self):
        self.result = []

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.inorder(root)
        return self.result

    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        self.result.append(root.val)
        self.inorder(root.right)
