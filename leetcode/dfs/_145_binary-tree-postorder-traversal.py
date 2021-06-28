#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : _145_binary-tree-postorder-traversal.py
Author       : miaoyc
Create date  : 2021/6/28 11:18 下午
Description  : 二叉树的后序遍历
"""

"""
给定一个二叉树，返回它的 后序 遍历。

示例:

输入: [1,null,2,3]  
   1
    \
     2
    /
   3 

输出: [3,2,1]
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

    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.post(root)
        return self.result

    def post(self, root):
        if not root:
            return
        self.post(root.left)
        self.post(root.right)
        self.result.append(root.val)
