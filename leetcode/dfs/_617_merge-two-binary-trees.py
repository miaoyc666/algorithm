#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : _617_merge-two-binary-trees.py
Author       : miaoyc
Create date  : 2021/7/12 11:53 下午
Description  : 合并二叉树
"""

"""
给定两个二叉树，想象当你将它们中的一个覆盖到另一个上时，两个二叉树的一些节点便会重叠。

你需要将他们合并为一个新的二叉树。合并的规则是如果两个节点重叠，那么将他们的值相加作为节点合并后的新值，否则不为 NULL 的节点将直接作为新二叉树的节点。

示例 1:

输入: 
	Tree 1                     Tree 2                  
          1                         2                             
         / \                       / \                            
        3   2                     1   3                        
       /                           \   \                      
      5                             4   7                  
输出: 
合并后的树:
	     3
	    / \
	   4   5
	  / \   \ 
	 5   4   7
注意: 合并必须从两个树的根节点开始。

"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):

    def mergeTrees(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: TreeNode
        """
        if not root1:
            return root2
        if not root2:
            return root1

        root1.val += root2.val
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)
        return root1

    #     # if not root1 and not root2:
    #     #     return
    #     # root = TreeNode(root1.val + root2.val)
    #     self.root = self.dfs(self.root, root1, root2)
    #     return self.root

    # def dfs(self, root, root1, root2):
    #     if not root1 and not root2:
    #         return

    #     if root1 and root2:
    #         if not root:
    #             root = TreeNode(0)
    #         root.val = root1.val + root2.val
    #         root.left =self.dfs(root.left, root1.left, root2.left)
    #         root.right = self.dfs(root.right, root1.right, root2.right)
    #         return root

    #     if root1 and not root2:
    #         return TreeNode(root1.val)

    #     if not root1 and root2:
    #         return TreeNode(root2.val)
