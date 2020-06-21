# date : 20/jun/20
# 1486. XOR Operation in an Array
# Easy

# 2

# 0

# Add to List

# Share
# Given an integer n and an integer start.

# Define an array nums where nums[i] = start + 2*i (0-indexed) and n == nums.length.

# Return the bitwise XOR of all elements of nums.

 

# Example 1:

# Input: n = 5, start = 0
# Output: 8
# Explanation: Array nums is equal to [0, 2, 4, 6, 8] where (0 ^ 2 ^ 4 ^ 6 ^ 8) = 8.
# Where "^" corresponds to bitwise XOR operator.
# Example 2:

# Input: n = 4, start = 3
# Output: 8
# Explanation: Array nums is equal to [3, 5, 7, 9] where (3 ^ 5 ^ 7 ^ 9) = 8.
# Example 3:

# Input: n = 1, start = 7
# Output: 7
# Example 4:

# Input: n = 10, start = 5
# Output: 2
 

# Constraints:

# 1 <= n <= 1000
# 0 <= start <= 1000
# n == nums.length

class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """

        bitwise = 0
        for i in range(n):
            bitwise = bitwise ^ start + 2*i
        
        return bitwise

Runtime: 24 ms, faster than 100.00% of Python online submissions for XOR Operation in an Array.
Memory Usage: 12.7 MB, less than 100.00% of Python online submissions for XOR Operation in an Array.