# 买卖股票问题

### 最佳买卖股票的时机Ⅰ
- 题目：[best-time-to-buy-and-sell-stock](../../leetcode/python/dp/_121_best-time-to-buy-and-sell-stock.py)
- 难度：简单
- 问题分类：dp
- 解题思路：分三步走，第一步记录【今天之前买入的最小市值和最大盈利】； 第二步是计算【今天之前最小值买入，今天卖出的获利】，也即【今天卖出的最大获利】，注意要从第二天开始迭代计算；第三步是比较【每天的最大获利】，取最大值即可。

### 最佳买卖股票的时机Ⅱ
- 题目：[best-time-to-buy-and-sell-stock-ii](../../leetcode/python/greedy/_122_best-time-to-buy-and-sell-stock-ii.py)
- 难度：中等
- 问题分类greedy
- 解题思路：贪心算法，由于一天内可以多次买卖，所以只要后一天的价格比前一天高，有利润即卖出，利润和即为最大利润。

