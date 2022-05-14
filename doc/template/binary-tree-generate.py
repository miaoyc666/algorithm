#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : binary-tree-generate.py
Author       : miaoyc
Create date  : 2022/05/14 22:03 下午
Description  : 二叉树的生成
"""

"""
根据数组生成二叉树，采用二叉树的特性如下：
假设父节点的下标是i，那么左孩子的下标是2i+1，右孩子的下标是2i+2
"""

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    def generate(self, vals):
        """
        :param vals: List
        :rtype: TreeNode
        """
        if not vals:
            return None
        queue = []
        length = len(vals)
        root = TreeNode(vals[0])
        queue.append(root)
        index = 0
        while queue:
            cur = queue.pop(0)
            if not cur:
                index += 1
                continue
            if 2 * index + 1 < length:
                cur.left = TreeNode(vals[2 * index + 1]) if vals[2 * index + 1] else None
            if 2 * index + 2 < length:
                cur.right = TreeNode(vals[2 * index + 2]) if vals[2 * index + 2] else None
            index += 1
            queue.append(cur.left)
            queue.append(cur.right)
        return root


if __name__ == "__main__":
    root_ = Solution().generate([1, 2, 3, 4])
    print(root_.val)
    print(root_.left.val)
    print(root_.right.val)
    print(root_.left.left.val)

