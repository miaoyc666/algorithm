#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : _19_remove-nth-node-from-end-of-list.py
Author       : miaoyc
Create date  : 2021/7/23 11:45 下午
Description  : 删除链表的倒数第 N 个结点
"""

"""
给你一个链表，删除链表的倒数第n个结点，并且返回链表的头结点。

进阶：你能尝试使用一趟扫描实现吗？

示例 1：


输入：head = [1,2,3,4,5], n = 2
输出：[1,2,3,5]
示例 2：

输入：head = [1], n = 1
输出：[]
示例 3：

输入：head = [1,2], n = 1
输出：[1]

提示：

链表中结点的数目为 sz
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):

    def __init__(self):
        self.count = 0

    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # 利用递归从后往前进行计数
        if not head:
            return
        head.next = self.removeNthFromEnd(head.next, n)
        self.count += 1
        if self.count == n:
            return head.next
        return head


