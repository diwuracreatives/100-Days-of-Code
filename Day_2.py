"""
100 Days of Code - Day 2

Topic:
-----
Array/Sliding Window

Question:
---------
Minimum size subarray sum
Given an array of positive integers nums and a positive integer target, return the minimal length of a 
subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

Solution:
---------
"""
#SOLUTION 1
def min_size_subarray_sum(nums, target):
    s = 0
    win_sum = len(nums)
    
    for i in range(len(nums)):
        for j in range(len(nums)):
            if sum(nums[i:j]) == target:
               s = sum(nums[i:j])
               win_sum = min(win_sum, s)
               print(nums[i:j])
    if s == 0:
        return s
    return win_sum

#SOLUTION 2
def min_size_subarray_sum(nums, target):
    l, r = 0, 0
    total = 0
    min_length = float("inf")
    
    for i in range(len(nums)):
        total += nums[i]
        while total >= target:
            min_length = min(min_length, i - l + 1)
            total -= nums[l]
            l += 1
    return 0 if min_length == float("inf") else min_length
  
print(min_size_subarray_sum([2, 3, 1, 2, 4, 3], 6))
print(min_size_subarray_sum([1,4,4], 3))
"""
Reflection:
-----------
Learnt about optimizing my code from O(n2) to O(n) using sliding window function.

Additional Notes:
-----------------
Leetcode Link - https://leetcode.com/problems/minimum-size-subarray-sum/

"""
