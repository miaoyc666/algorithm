#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : _3_longest-substring-without-repeating-characters.py
Author       : miaoyc
Create date  : 2021/7/24 23:52
Update date  : 2023/4/21 23:17
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
其实就是一个队列,比如例题中的 abcabcbb，进入这个队列（窗口）为 abc 满足题目要求，当再进入 a，队列变成了 abca，这时候不满足要求。
所以，我们要移动这个队列！
如何移动？
我们只要把队列的左边的元素移出就行了，直到满足题目要求！
一直维持这样的队列，找出队列出现最长的长度时候，求出解！

时间复杂度：O(n)O(n)
"""

# 用python实现一个函数，获取字符串内不含有重复字符的最长子串的长度。
# 例如：输入字符串“abcabcbb”，输出结果为3，因为“abc”是最长的不含重复字符的子串。
# 要求：时间复杂度为O(n)


def get_longest_substring_length(s):
    """
    这个是github copilot写的，我也不知道为什么这么写，但是确实是对的
    :param s:
    :return:
    """
    if not s:
        return 0
    seen = set()
    cur_len, max_len = 0, 0
    for i in range(len(s)):
        cur_len += 1
        while s[i] in seen:
            seen.remove(s[i - cur_len])
            cur_len -= 1
        seen.add(s[i])
        max_len = max(max_len, cur_len)
    return max_len


class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        什么是滑动窗口？
        其实就是一个队列,比如例题中的 abcabcbb，进入这个队列（窗口）为 abc 满足题目要求，当再进入 a，队列变成了 abca，这时候不满足要求。
        所以，我们要移动这个队列！
        如何移动？
        我们只要把队列的左边的元素移出就行了，直到满足题目要求！
        一直维持这样的队列，找出队列出现最长的长度时候，求出解！
        时间复杂度：O(n)
        """
        if not s:
            return 0
        seen = set()
        cur_len, max_len, left = 0, 0, 0
        for i in range(len(s)):
            cur_len += 1
            # while循环为了找到第一个s[i]的位置，把s[i]之前的都移除
            while s[i] in seen:
                seen.remove(s[left])
                left += 1
                cur_len -= 1
            if cur_len > max_len:
                max_len = cur_len
            seen.add(s[i])
        return max_len


if __name__ == "__main__":
    print(Solution().lengthOfLongestSubstring("dvdf"))
