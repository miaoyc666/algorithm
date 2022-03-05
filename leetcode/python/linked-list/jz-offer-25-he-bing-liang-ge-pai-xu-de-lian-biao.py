#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : jz-offer-25-he-bing-liang-ge-pai-xu-de-lian-biao.py
Author       : miaoyc
Create date  : 2022/3/5 10:27 PM
Description  : 合并两个排序的链表
"""

"""
难度：简单

与21 merge-two-sorted-lists题目重复
 
输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。

示例1：
输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
限制：

0 <= 链表长度 <= 1000
"""

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode()
        pre = head
        while l1 and l2:
            if l1.val <= l2.val:
                pre.next = l1
                l1 = l1.next
            else:
                pre.next = l2
                l2 = l2.next
            pre = pre.next
        pre.next = l1 if l1 else l2
        return head.next

