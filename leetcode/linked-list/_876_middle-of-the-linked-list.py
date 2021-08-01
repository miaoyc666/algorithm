#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : _876_middle-of-the-linked-list.py
Author       : miaoyc
Create date  : 2021/7/23 11:27 下午
Description  : 链表的中间节点
"""

"""
给定一个头结点为 head的非空单链表，返回链表的中间结点。

如果有两个中间结点，则返回第二个中间结点。



示例 1：

输入：[1,2,3,4,5]
输出：此列表中的结点 3 (序列化形式：[3,4,5])
返回的结点值为 3 。 (测评系统对该结点序列化表述是 [3,4,5])。
注意，我们返回了一个 ListNode 类型的对象 ans，这样：
ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, 以及 ans.next.next.next = NULL.
示例2：

输入：[1,2,3,4,5,6]
输出：此列表中的结点 4 (序列化形式：[4,5,6])
由于该列表有两个中间结点，值分别为 3 和 4，我们返回第二个结点。


提示：

给定链表的结点数介于1和100之间。
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import copy


class Solution(object):

    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        tmp = copy.deepcopy(head)
        # count
        count = 0
        while tmp.next:
            count += 1
            tmp = tmp.next
        count += 1
        # find
        length = count / 2
        while length > 0:
            length -= 1
            head = head.next
        return head