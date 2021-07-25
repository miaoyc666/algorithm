#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : _3_longest-substring-without-repeating-characters.py
Author       : miaoyc
Create date  : 2021/7/24 23:52
Description  : 无重复字符的最长子串
"""

"""
给定一个字符串 s ，请你找出其中不含有重复字符的最长子串的长度。

示例1:

输入: s = "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是"wke"，所以其长度为 3。
    请注意，你的答案必须是 子串 的长度，"pwke"是一个子序列，不是子串。
示例 4:

输入: s = ""
输出: 0

提示：

0 <= s.length <= 5 * 104
s由英文字母、数字、符号和空格组成
"""

"""
什么是滑动窗口？

其实就是一个队列,比如例题中的 abcabcbb，进入这个队列（窗口）为 abc 满足题目要求，当再进入 a，队列变成了 abca，这时候不满足要求。所以，我们要移动这个队列！

如何移动？

我们只要把队列的左边的元素移出就行了，直到满足题目要求！

一直维持这样的队列，找出队列出现最长的长度时候，求出解！

时间复杂度：O(n)O(n)
"""


class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        什么是滑动窗口？

        其实就是一个队列,比如例题中的 abcabcbb，进入这个队列（窗口）为 abc 满足题目要求，当再进入 a，队列变成了 abca，这时候不满足要求。所以，我们要移动这个队列！

        如何移动？

        我们只要把队列的左边的元素移出就行了，直到满足题目要求！

        一直维持这样的队列，找出队列出现最长的长度时候，求出解！

        时间复杂度：O(n)
        """
        a = set()
        b = []
        max_len = 0
        for i in s:
            if i in a:
                a.add(i)
                b.append(i)
                while b and b[0] in a:
                    print(b)
                    a.remove(b.pop(0))
            a.add(i)
            b.append(i)
            if len(b) >= max_len:
                max_len = len(b)
        return max_len


if __name__ == "__main__":
    print(Solution().lengthOfLongestSubstring("dvdf"))
