#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : _108_convert-sorted-array-to-binary-search-tree.py
Author       : miaoyc
Create date  : 2021/8/29 11:13 下午
Description  : 将有序数组转换为二叉搜索树
"""

"""
给你一个整数数组 nums ，其中元素已经按 升序 排列，请你将其转换为一棵 高度平衡 二叉搜索树。
高度平衡 二叉树是一棵满足「每个节点的左右两个子树的高度差的绝对值不超过 1 」的二叉树。

示例 1：
输入：nums = [-10,-3,0,5,9]
输出：[0,-3,9,-10,null,5]
解释：[0,-10,5,null,-3,null,9] 也将被视为正确答案：

示例 2：
输入：nums = [1,3]
输出：[3,1]
解释：[1,3] 和 [3,1] 都是高度平衡二叉搜索树。

提示：
1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums 按 严格递增 顺序排列
"""

from typing import List

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def get_min(left, right):
            # 总是选择中间位置左边的数字作为根节点
            if left > right:
                return None
            mid = (left+right) // 2
            root = TreeNode(nums[mid])
            root.left = get_min(left, mid-1)
            root.right = get_min(mid+1, right)
            return root
        return get_min(0, len(nums)-1)
