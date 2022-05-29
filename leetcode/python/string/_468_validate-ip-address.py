#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : _468_validate-ip-address.py
Author       : miaoyc
Create date  : 2022/5/29 21:57
Description  : 验证IP地址
"""

"""
难度：中等

给定一个字符串queryIP。如果是有效的 IPv4 地址，返回 "IPv4" ；如果是有效的 IPv6 地址，返回 "IPv6" ；如果不是上述类型的 IP 地址，返回 "Neither" 。
有效的IPv4地址 是 “x1.x2.x3.x4” 形式的IP地址。 其中0 <= xi<= 255且xi不能包含 前导零。例如:“192.168.1.1”、 “192.168.1.0” 为有效IPv4地址， “192.168.01.1” 为无效IPv4地址; “192.168.1.00” 、 “192.168@1.1” 为无效IPv4地址。
一个有效的IPv6地址是一个格式为“x1:x2:x3:x4:x5:x6:x7:x8” 的IP地址，其中:
1 <= xi.length <= 4
xi是一个 十六进制字符串 ，可以包含数字、小写英文字母( 'a' 到 'f' )和大写英文字母( 'A' 到 'F' )。
在xi中允许前导零。
例如 "2001:0db8:85a3:0000:0000:8a2e:0370:7334" 和 "2001:db8:85a3:0:0:8A2E:0370:7334" 是有效的 IPv6 地址，而 "2001:0db8:85a3::8A2E:037j:7334" 和 "02001:0db8:85a3:0000:0000:8a2e:0370:7334" 是无效的 IPv6 地址。

示例 1：
输入：queryIP = "172.16.254.1"
输出："IPv4"
解释：有效的 IPv4 地址，返回 "IPv4"

示例 2：
输入：queryIP = "2001:0db8:85a3:0:0:8A2E:0370:7334"
输出："IPv6"
解释：有效的 IPv6 地址，返回 "IPv6"

示例 3：
输入：queryIP = "256.256.256.256"
输出："Neither"
解释：既不是 IPv4 地址，又不是 IPv6 地址

提示：
queryIP 仅由英文字母，数字，字符 '.' 和 ':' 组成。
"""


class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        if "." in queryIP:
            s_list = queryIP.split(".")
            if len(s_list) != 4:
                return "Neither"
            if s_list[0].isdigit() and int(s_list[0]) == 0:
                return "Neither"
            for i, v in enumerate(s_list):
                if not v.isdigit():
                    return "Neither"
                if i == 0 and int(v) == 0:
                    return "Neither"
                if len(v) != 1 and v[0] == "0":
                    return "Neither"
                if int(v) < 0 or int(v) > 255:
                    return "Neither"
            return "IPv4"
        else:
            s_list = queryIP.split(":")
            if len(s_list) != 8:
                return "Neither"
            for v in s_list:
                if len(v) <= 0 or len(v) > 4:
                    return "Neither"
                if not all(ch in '0123456789abcdefABCDEF' for ch in v):
                    return "Neither"
            return "IPv6"
