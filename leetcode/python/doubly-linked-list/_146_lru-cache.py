#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : _146_lru-cache.py
Author       : miaoyc
Create date  : 2021/8/9 11:25 下午
Description  : LRU 缓存机制
"""

"""
难度：中等

运用你所掌握的数据结构，设计和实现一个 LRU (最近最少使用) 缓存机制 。
实现 LRUCache 类：
LRUCache(int capacity) 以正整数作为容量capacity 初始化 LRU 缓存
int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
void put(int key, int value)如果关键字已经存在，则变更其数据值；如果关键字不存在，则插入该组「关键字-值」。当缓存容量达到上限时，它应该在写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间。
进阶：你是否可以在O(1) 时间复杂度内完成这两种操作？


示例：
输入
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
输出
[null, null, null, 1, null, -1, null, -1, 3, 4]

解释
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // 缓存是 {1=1}
lRUCache.put(2, 2); // 缓存是 {1=1, 2=2}
lRUCache.get(1);    // 返回 1
lRUCache.put(3, 3); // 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
lRUCache.get(2);    // 返回 -1 (未找到)
lRUCache.put(4, 4); // 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
lRUCache.get(1);    // 返回 -1 (未找到)
lRUCache.get(3);    // 返回 3
lRUCache.get(4);    // 返回 4

提示：
1 <= capacity <= 3000
0 <= key <= 10000
0 <= value <= 105
最多调用 2 * 105 次 get 和 put
"""


class DLinkedNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    # 思路
    # 核心：最近最少使用缓存，仅保存最近使用的缓存数据
    # 核心：使用双向链表，可以高效在队首和队尾增删数据。遍历队列是O(n), 借助字典实现O(1)查找节点，字典key为节点key，value为节点对象
    # 1.使用缓存时，将缓存移动到队首；
    # 2.新增缓存时，将缓存加入在对首，若此时队列长度超限，移除队尾元素；
    # 3.更新缓存时，找到key对应的元素，更新value，将元素移动到队首；

    # 核心属性
    # 1.cache，节点映射
    # 2.head和tail, 头结点和尾节点构建而成的双向链表

    # 可复用函数
    # 1.添加数据到头部节点addToHead
    # 2.删除节点removeNode

    def __init__(self, capacity: int):
        # 初始化时构建两个元素的双向链表，用做链表的头尾节点
        self.cache = {}
        self.capacity = capacity
        self.size = 0
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_2_head(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def remove_tail(self):
        node = self.tail.prev
        self.remove_node(node)
        return node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # 移动元素到队首
        node = self.cache[key]
        self.move_node_2_head(node)
        return node.value

    def move_node_2_head(self, node):
        # 核心是先解决node的前后关联，再解决node两侧节点对node的关联
        # 可复用删除节点与在头结点添加节点的函数
        # 先删除当前节点，再在头结点添加节点
        self.remove_node(node)
        self.add_2_head(node)

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.update(key, value)
        else:
            self.insert(key, value)

    def insert(self, key, value):
        node = DLinkedNode(key, value)
        self.cache[key] = node
        self.add_2_head(node)
        self.size += 1
        if self.size > self.capacity:
            # 超出容量时删除尾部节点, 删除映射表中的缓存节点，同时size-1
            removed = self.remove_tail()
            self.cache.pop(removed.key)
            self.size -= 1

    def update(self, key, value):
        node = self.cache[key]
        node.value = value
        self.move_node_2_head(node)
