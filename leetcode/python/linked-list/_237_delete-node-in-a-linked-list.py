#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : _237_delete-node-in-a-linked-list.py
Author       : miaoyc
Create date  : 2021/10/19 11:45 下午
Description  : 删除链表中的节点
"""

"""
请编写一个函数，使其可以删除某个链表中给定的（非末尾）节点。传入函数的唯一参数为 要被删除的节点 。
现有一个链表 --head =[4,5,1,9]，它可以表示为:
示例 1：
输入：head = [4,5,1,9], node = 5
输出：[4,1,9]
解释：给定你链表中值为5的第二个节点，那么在调用了你的函数之后，该链表应变为 4 -> 1 -> 9.

示例 2：
输入：head = [4,5,1,9], node = 1
输出：[4,5,9]
解释：给定你链表中值为1的第三个节点，那么在调用了你的函数之后，该链表应变为 4 -> 5 -> 9.

提示：
链表至少包含两个节点。
链表中所有节点的值都是唯一的。
给定的节点为非末尾节点并且一定是链表中的一个有效节点。
不要从你的函数中返回任何结果。
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # 解题思路：
        # 这道题没有给出链表的头节点，而是直接给出要删除的节点，让我们进行原地删除。
        # 我们对于该节点的前一个节点一无所知，所以无法直接执行删除操作。因此，我们将要删除节点的 next 节点的值赋值给要删除的节点，转而去删除 next 节点，从而达成目的。
        node.val = node.next.val
        node.next = node.next.next
