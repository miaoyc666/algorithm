#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : _2_add-two-numbers.py
Author       : miaoyc
Create date  : 2021/10/23 11:29 下午
Description  : 两数相加
"""

"""
给你两个非空 的链表，表示两个非负的整数。它们每位数字都是按照逆序的方式存储的，并且每个节点只能存储一位数字。
请你将两个数相加，并以相同形式返回一个表示和的链表。
你可以假设除了数字 0 之外，这两个数都不会以 0开头。

示例 1：
输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807.

示例 2：
输入：l1 = [0], l2 = [0]
输出：[0]

示例 3：
输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
输出：[8,9,9,9,0,0,0,1]

提示：
每个链表中的节点数在范围 [1, 100] 内
0 <= Node.val <= 9
题目数据保证列表表示的数字不含前导零
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sum_ = self.convert2num(l1) + self.convert2num(l2)
        return self.convert2linkedList(sum_)

    def convert2linkedList(self, num_: int):
        num_str = str(num_)
        head = ListNode(int(num_str[-1]))
        l = head
        for i in range(len(num_str) - 2, -1, -1):
            node = ListNode(int(num_str[i]))
            head.next = node
            head = node
        return l

    def convert2num(self, l: ListNode):
        tmp = []
        head = l
        while head:
            tmp.append(head.val)
            head = head.next
        num = 0
        for i in range(len(tmp)):
            j = tmp.pop()
            num = num * 10 + j
        return num
