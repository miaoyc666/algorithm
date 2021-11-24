/*
File name    : _1_two-sum.rs
Author       : miaoyc
Create date  : 2021/9/1 10:49 下午
Update date  : 2021/11/22 23:47
Description  : 两数之和
*/

/*
给定一个整数数组 nums和一个目标值 target，请你在该数组中找出和为目标值的那两个整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

示例:
给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
*/

use std::collections::HashMap;

impl Solution {
    
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut map: HashMap<i32, usize> = HashMap::new();
        for i in 0..nums.len() {
            let complement = target - nums[i];
            if map.contains_key(&complement) {
                return vec![i as i32, map[&complement] as i32];
            }
            map.insert(nums[i], i);
        }
        return vec![];
    }


    pub fn two_sum_old(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut res = vec![];
        let mut cache = HashMap::new();

        for (index, item) in nums.iter().enumerate() {
            let sub = target - *item;

            match cache.get(item) {
                Some(pre_index) => {
                    res.push(*pre_index);
                    res.push(index as i32);
                    return res
                },
                None => {
                    cache.insert(sub, index as i32);
                },
            }
        }
        res
    }
}


