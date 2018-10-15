#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
hihocoder 1015 kmp 算法实现
"""


def kmp_match(s, p):
    """
    KMP实现, 返回p在s中命中次数
    :param s:
    :param p:
    :return:
    """
    m = len(s)
    n = len(p)
    cur = 0
    count = 0
    table = partial_table(p)
    while cur <= m - n:
        for i in range(n):
            if s[i + cur] != p[i]:
                cur += max(i - table[i - 1], 1)
                break
        else:
            count += 1
            cur += i
    return count


def partial_table(p):
    """
    生成部分匹配表
    :param p:
    :return:
    """
    prefix = set()
    ret = [0]
    for i in range(1, len(p)):
        prefix.add(p[:i])
        postfix = {p[j:i + 1] for j in range(1, i + 1)}
        match_value = max(map(len, prefix & postfix)) if prefix & postfix else 0
        ret.append(match_value)
    return ret


def main():
    """
    main
    :return:
    """
    while True:
        try:
            res = []
            group_count = int(raw_input())
            for i in xrange(group_count):
                res.append(kmp_match(str(raw_input()), str(raw_input())))
            for i in res:
                print i

        except EOFError:
            break


if __name__ == "__main__":
    main()
