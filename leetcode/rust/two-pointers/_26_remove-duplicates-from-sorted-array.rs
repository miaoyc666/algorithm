/*
File name    : _26_remove-duplicates-from-sorted-array.rs
Author       : miaoyc
Create date  : 2021/9/6 11:31 下午
Description  : 删除有序数组中的重复项
*/

/*
给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。
不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

说明:
为什么返回数值是整数，但输出的答案是数组呢?
请注意，输入数组是以「引用」方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。

你可以想象内部操作如下:
// nums 是以“引用”方式传递的。也就是说，不对实参做任何拷贝
int len = removeDuplicates(nums);

// 在函数里修改输入数组对于调用者是可见的。
// 根据你的函数返回的长度, 它会打印出数组中 该长度范围内 的所有元素。
for (int i = 0; i < len; i++) {
  print(nums[i]);
}

示例 1：
输入：nums = [1,1,2]
输出：2, nums = [1,2]
解释：函数应该返回新的长度 2 ，并且原数组 nums 的前两个元素被修改为 1, 2 。不需要考虑数组中超出新长度后面的元素。

示例 2：
输入：nums = [0,0,1,1,1,2,2,3,3,4]
输出：5, nums = [0,1,2,3,4]
解释：函数应该返回新的长度 5 ， 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4 。不需要考虑数组中超出新长度后面的元素。

提示：
0 <= nums.length <= 3 * 104
-104 <= nums[i] <= 104
nums 已按升序排列
*/

/*
解题思路
双指针，快慢指针的解法
排序后的数据nums, 放置两个指针i和j，其中i是慢指针，j是快指针。遍历数组做一下判断
1.当nums[i]=num[j]时，递增j以跳过重复项；
2.当nums[i]!=num[j]时，把nums[j]的值复制到nums[i+1], 然后i+1；
重复以上过程，知道j到达数组末位为止。
*/

impl Solution {
    pub fn remove_duplicates(nums: &mut Vec<i32>) -> i32 {
        if nums.len() == 0 {
            return 0
        }
        let mut i = 0;
        for j in 0..nums.len() {
            if nums[i] != nums[j] {
                // 此处为判断是否所有数据都不重复，不重复的情况下就没有必要进行一次赋值
                if i + 1 < j {
                    nums[i+1] = nums[j];
                }
                i += 1;
            }
        }
        return (i + 1) as i32;
    }
}
