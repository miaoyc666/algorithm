/*
File name    : _136_single-number.rs
Author       : miaoyc
Create date  : 2021/10/28 10:12 下午
Description  : 只出现一次的数字
*/

/*
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
说明：
你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

示例 1:
输入: [2,2,1]
输出: 1

示例2:
输入: [4,1,2,1,2]
输出: 4
*/

impl Solution {
    pub fn single_number(nums: Vec<i32>) -> i32 {
        /*
        算法思路：
        1、交换律：a ^ b ^ c <=> a ^ c ^ b
        2、任何数于0异或为任何数 0 ^ n => n
        3、相同的数异或为0: n ^ n => 0
        解决方案：
        将list内数据全部异或即可得到单独的数
        */
        let mut single_num = 0;
        for i in 0..nums.len() {
            single_num ^= nums[i];
        }
        return single_num as i32;
    }
}
