#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : _449_serialize-and-deserialize-bst.py
Author       : miaoyc
Create date  : 2022/5/16 11:42 
Description  : 序列化和反序列化二叉搜索树
"""

"""
难度：中等

序列化是将数据结构或对象转换为一系列位的过程，以便它可以存储在文件或内存缓冲区中，或通过网络连接链路传输，以便稍后在同一个或另一个计算机环境中重建。
设计一个算法来序列化和反序列化 二叉搜索树 。 对序列化/反序列化算法的工作方式没有限制。 您只需确保二叉搜索树可以序列化为字符串，并且可以将该字符串反序列化为最初的二叉搜索树。
编码的字符串应尽可能紧凑。

示例 1：
输入：root = [2,1,3]
输出：[2,1,3]

示例 2：
输入：root = []
输出：[]

提示：
树中节点数范围是 [0, 104]
0 <= Node.val <= 104
题目数据 保证 输入的树是一棵二叉搜索树。
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque


class Codec:

    def serialize(self, root):
        """
        Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        queue = deque([root])
        s = ""
        while len(queue) > 0:
            size = len(queue)
            for i in range(size):
                head = queue.popleft()
                if head:
                    s += str(head.val)
                    queue.append(head.left)
                    queue.append(head.right)
                else:
                    s += "N"
                s += " "
        return s

    def deserialize(self, data):
        """
        Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        vals = data.split()
        if not vals:
            return None
        if vals[0] == 'N':
            return None
        root = TreeNode(vals[0])
        queue = deque([root])
        index = 1
        while queue:
            cur = queue.popleft()
            if vals[index] != "N":
                cur.left = TreeNode(vals[index])
                queue.append(cur.left)
            index += 1
            if vals[index] != "N":
                cur.right = TreeNode(vals[index])
                queue.append(cur.right)
            index += 1
        return root


# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
