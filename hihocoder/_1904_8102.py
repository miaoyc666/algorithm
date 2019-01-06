#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
描述
"都8102年了"是2018年网络流行语，8102是将今年年份2018的各位数字倒排的结果，常用来表达“都这个年头了，怎么还有某某事情发生"之意。
这个梗的关键在于将年份各位数字倒排之后，得到一个非常遥远的未来年份。小Hi想知道，哪些年份适合使用这个梗。
具体来说，一个年份Y，倒排之后得到年份X，如果X-Y>=1000，我们就认为Y适合这个梗。
给定起止年份，请你判断这段时间内有几个年份适合这个梗。

输入
两个正整数代表年份，A和B。

1000 <= A <= B <= 9999

输出
一个整数代表答案

样例输入
2018 2020

样例输出
2
"""


def reverse_num(num):
    """
    反转数字
    :param num:
    :return:
    """
    return int(str(num)[::-1])


def main():
    """
    main
    :return:
    """
    count = 0
    (start, end) = (int(x) for x in raw_input().split())
    for num in xrange(start, end+1):
        if reverse_num(num) - num >= 1000:
            count += 1
    print count


if __name__ == "__main__":
    main()
