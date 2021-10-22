#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : _203_remove-linked-list-elements.py
Author       : miaoyc
Create date  : 2021/10/21 11:51 下午
Description  : 
"""

"""
给你一个链表的头节点 head 和一个整数 val ，请你删除链表中所有满足 Node.val == val 的节点，并返回 新的头节点 。

示例 1：
输入：head = [1,2,6,3,4,5,6], val = 6
输出：[1,2,3,4,5]

示例 2：
输入：head = [], val = 1
输出：[]

示例 3：
输入：head = [7,7,7,7], val = 7
输出：[]
"""

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def removeElements(self, head: ListNode, val: int) -> ListNode:
        """
        解题思路：
        链表的定义具有递归的性质，因此链表题目常可以用递归的方法求解。
        这道题要求删除链表中所有节点值等于特定值的节点，可以用递归实现。

        对于给定的链表，首先对除了头节点head以外的节点进行删除操作，然后判断head的节点值是否等于给定的val。
        如果head的节点值等于val，则head需要被删除，因此删除操作后的头节点为head.next；
        如果head的节点值不等于val，则head保留，因此删除操作后的头节点还是head。上述过程是一个递归的过程。

        递归的终止条件是head为空，此时直接返回head。
        当head不为空时，递归地进行删除操作，然后判断head的节点值是否等于val并决定是否要删除head。
        """
        if not head:
            return
        head.next = self.removeElements(head.next, val)
        if head.val == val:
            return head.next
        else:
            return head
