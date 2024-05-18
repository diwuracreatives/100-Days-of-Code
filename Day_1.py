"""
100 Days of Code - Day 1

Topic:
-----
Array

Question:
---------
Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.
You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

Solution:
---------
"""
def firstMissingPositive(nums):
    c = set(nums)
    res = 1

    while res in c:
            res += 1
    return res

print(firstMissingPositive(nums = [3,4,-1,1]))

"""
Reflection:
-----------
Learnt about optimizing the runtime by using set() function.

Additional Notes:
-----------------
Leetcode Link - https://leetcode.com/problems/first-missing-positive/

"""
