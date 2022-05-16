#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : _297_serialize-and-deserialize-binary-tree.py
Author       : miaoyc
Create date  : 2022/5/11 23:17
Description  : 二叉树的序列化与反序列化
"""

"""
难度：困难

序列化是将一个数据结构或者对象转换为连续的比特位的操作，进而可以将转换后的数据存储在一个文件或者内存中，同时也可以通过网络传输到另一个计算机环境，采取相反方式重构得到原数据。
请设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。
提示: 输入输出格式与 LeetCode 目前使用的方式一致，详情请参阅LeetCode 序列化二叉树的格式。你并非必须采取这种方式，你也可以采用其他的方法解决这个问题。

示例 1：
输入：root = [1,2,3,null,null,4,5]
输出：[1,2,3,null,null,4,5]

示例 2：
输入：root = []
输出：[]

示例 3：
输入：root = [1]
输出：[1]

示例 4：
输入：root = [1,2]
输出：[1,2]

提示：
树中结点数在范围 [0, 104] 内
-1000 <= Node.val <= 1000
"""

# from collections import deque


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
解题思路：
1.二叉搜索树的特点为左孩子节点比父节点小，右孩子节点比父节点大，可以利用该特性进行反序列化；
2.序列化时使用后续遍历，可以保证root节点在序列化列表的末尾；
3.反序列化时，每次递归遍历序列化数据中的一条数据。
"""

import cmath


class Codec:

    def serialize(self, root: TreeNode) -> str:
        arr = []

        def postOrder(root: TreeNode) -> None:
            if root is None:
                return
            postOrder(root.left)
            postOrder(root.right)
            arr.append(root.val)
        postOrder(root)
        return ' '.join(map(str, arr))

    def deserialize(self, data: str) -> TreeNode:
        arr = list(map(int, data.split()))

        def construct(lower: int, upper: int) -> TreeNode:
            if arr == [] or arr[-1] < lower or arr[-1] > upper:
                return None
            val = arr.pop()
            root = TreeNode(val)
            root.right = construct(val, upper)
            root.left = construct(lower, val)
            return root
        return construct(-cmath.inf, cmath.inf)


# class Codec:
#
#     def serialize(self, root):
#         """
#         Encodes a tree to a single string.
#         :type root: TreeNode
#         :rtype: str
#         """
#         queue = deque([root])
#         s = ""
#         while len(queue) > 0:
#             size = len(queue)
#             for i in range(size):
#                 head = queue.popleft()
#                 if head:
#                     s += str(head.val)
#                     queue.append(head.left)
#                     queue.append(head.right)
#                 else:
#                     s += "N"
#                 s += " "
#         return s
#
#     def deserialize(self, data):
#         """
#         Decodes your encoded data to tree.
#         :type data: str
#         :rtype: TreeNode
#         """
#         vals = data.split()
#         if not vals:
#             return None
#         if vals[0] == 'N':
#             return None
#         root = TreeNode(vals[0])
#         queue = deque([root])
#         index = 1
#         while queue:
#             cur = queue.popleft()
#             if vals[index] != "N":
#                 cur.left = TreeNode(vals[index])
#                 queue.append(cur.left)
#             index += 1
#             if vals[index] != "N":
#                 cur.right = TreeNode(vals[index])
#                 queue.append(cur.right)
#             index += 1
#         return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
