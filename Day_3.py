"""
100 Days of Code - Day 3

Topic:
-----
Array/Sliding Window

Question:
---------
Minimum-swaps-to-group-all-1s-together-11
A swap is defined as taking two distinct positions in an array and swapping the values in them.
A circular array is defined as an array where we consider the first element and the last element to be adjacent.
Given a binary circular array nums, return the minimum number of swaps required to group all 1's present in the array together at any location.

Solution:
---------
"""
def min_swaps(arr):
     total_count = 0

     for i in range(len(arr)):
          if arr[i] == 1:
               total_count += 1
  

     curr_count = 0
     max_count = 0
     i, j = 0,0
     
     while(j < len(arr)):
          
          if arr[j] == 1:
               curr_count += 1
          print(curr_count)
          if ((j - i + 1) == total_count):
               print()
               max_count = max(max_count, curr_count)
               if arr[i] == 1:
                    curr_count -=1
         
               i += 1
          print(arr[j:])    
          j += 1
     return total_count - max_count

print(min_swaps([1, 0, 1, 0, 1, 1]))
"""
Reflection:
-----------
Learnt about optimizing my code from O(n2) to O(n) using sliding window function.

Additional Notes:
-----------------
Leetcode Link - https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together-ii/

"""
