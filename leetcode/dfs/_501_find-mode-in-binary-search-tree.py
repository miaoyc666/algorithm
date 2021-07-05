#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : _501_find-mode-in-binary-search-tree.py
Author       : miaoyc
Create date  : 2021/7/4 3:01 下午
Description  : 二叉搜索树中的众数
"""

"""
给定一个有相同值的二叉搜索树（BST），找出 BST 中的所有众数（出现频率最高的元素）。

假定 BST 有如下定义：

结点左子树中所含结点的值小于等于当前结点的值
结点右子树中所含结点的值大于等于当前结点的值
左子树和右子树都是二叉搜索树
例如：
给定 BST [1,null,2,2],

   1
    \
     2
    /
   2
返回[2].

提示：如果众数超过1个，不需考虑输出顺序

进阶：你可以不使用额外的空间吗？（假设由递归产生的隐式调用栈的开销不被计算在内）
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):

    def __init__(self):
        self.data = []
        self.same_count = 0
        self.max_count = 0
        self.result = []

    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.inorder(root)
        return self.result

    def diff(self, root):
        if len(self.data) == 1:
            self.same_count = 1
            self.max_count = 1
            self.result = [root.val]
        elif self.data[-1] == self.data[-2]:
            self.same_count += 1
            if self.same_count > self.max_count:
                self.max_count = self.same_count
                self.result = [root.val]
            elif self.same_count == self.max_count:
                self.result.append(root.val)
        elif self.data[-1] != self.data[-2]:
            self.same_count = 1
            if self.max_count == 1:
                self.result.append(root.val)

    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        self.data.append(root.val)
        self.diff(root)
        self.inorder(root.right)
