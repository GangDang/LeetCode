#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#
import itertools

class Solution:
    def twoSum(self, nums: [int], target: int) -> [int]:
        hashmap={};
        for i ,item in enumerate(nums):
            minuend=target-item;
            if minuend in hashmap:
                return [hashmap[minuend],i];
            hashmap[item]=i;
        return None;
            
