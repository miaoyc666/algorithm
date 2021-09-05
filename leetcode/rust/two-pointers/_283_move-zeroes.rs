/*
File name    : _283_move-zeroes.rs
Author       : miaoyc
Create date  : 2021/9/5 11:49 下午
Description  : 
*/

/*
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

示例:
输入: [0,1,0,3,12]
输出: [1,3,12,0,0]
说明:

必须在原数组上操作，不能拷贝额外的数组。
尽量减少操作次数。
*/

impl Solution {
    pub fn move_zeroes(nums: &mut Vec<i32>) {
        let mut i = 0;
        let mut j = 0;
        // 不等于0的移动到前面
        for i in 0..mums.len() {
            if nums[i] != 0 {
                nums[i] = nums[j];
                j += 1;
            }
        }
        // 剩余部分全部置为0
        for k in j..nums.len() {
            nums[k] = 0;
        }
    }
}
