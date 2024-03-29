/*
File name    : _239_sliding-window-maximum.rs
Author       : miaoyc
Create date  : 2021/10/13 00:15 上午
Description  :
*/

/*
给你一个整数数组 nums，有一个大小为k的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k个数字。滑动窗口每次只向右移动一位。
返回滑动窗口中的最大值。

示例 1：
输入：nums = [1,3,-1,-3,5,3,6,7], k = 3
输出：[3,3,5,5,6,7]
解释：
滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

示例 2：
输入：nums = [1], k = 1
输出：[1]

示例 3：
输入：nums = [1,-1], k = 1
输出：[1,-1]

示例 4：
输入：nums = [9,11], k = 2
输出：[11]

示例 5：
输入：nums = [4,-2], k = 2
输出：[4]

提示：
1 <= nums.length <= 105
-104<= nums[i] <= 104
1 <= k <= nums.length
*/

/*
算法原理：使用双端队列实现一个单调递减队列，元素从队尾压入，从队尾或者队首弹出，直接取队首元素即可得到最大值。

算法流程：
1、给定的数组nums为空或这k为1，直接返回空数组；
2、处理前k个元素，初始化单调递减队列；
3、遍历数组，取件[k, nums.len())，在每一步执行3个操作：
- 清理队列，弹出所有小于当前值的元素（它们不可能是最大值）， 维持队列的单调递减
- 将当前元素从队尾压入队列
- 将最大值加入输出到数组
4、单调递减队列的处理函数如下：
- push函数：当队尾元素小于当前值，弹出队尾元素，重复此步骤，直到队列为空，然后再将当前值从队尾压入
- pop函数：当队首元素等于传入元素，弹出队首元素
- max函数：返回队列中的最大值，即队首元素
*/

use std::collections::VecDeque;

impl Solution {
    pub fn max_sliding_window(nums: Vec<i32>, k: i32) -> Vec<i32> {
        // 数组为空或者k为1，直接返回空数组
        if nums.len() == 0 || k == 1 {
            return nums;
        }

        let mut res: Vec<i32> = Vec::new();
        let mut deque: VecDeque<i32> = VecDeque::new();
        for i in 0..nums.len() {
            // 弹出队列中所有小于当前值的元素，然后再将当前值从队尾压入
            push(&mut deque, nums[i]);
            if (i as i32) > k - 1 {
                // 弹出队首元素，让滑动窗口内保持k个数字
                pop(&mut deque, nums[i - k as usize]);
                // 将最大值加入输出数组
                res.push(max(&deque);
            } else if (i as i32) == k - 1 {
                // 将前k个元素的最大值加入输出数组
                res.push(max(&deque));
            }
        }
        return res;
    }
}

fn push() {
}

fn pop() {
}

fn max() {
}
