'''
Question: https://leetcode.com/problems/house-robber/
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
'''

from typing import List

class Solution:
    """
    A class that contains different solutions to solve the 'House Robber' problem.
    """

    def rob_brute_force(self, nums: List[int]) -> int:
        """
        Brute Force Recursion (Exponential)
        ------------------------------------
        Recurrence Relation:
        maxMoney(i) = max(maxMoney(i-1), nums[i] + maxMoney(i-2))

        Base Cases:
        - If i < 0: return 0 (No house to rob)
        
        Time Complexity: O(2^n) - Exponential (TLE for large n)
        Space Complexity: O(n) - Due to recursion depth
        """
        def helper(i):
            if i < 0:
                return 0
            return max(helper(i - 1), nums[i] + helper(i - 2))

        return helper(len(nums) - 1)

    
    def rob_memoization(self, nums: List[int]) -> int:
        """
        Memoization (Top-Down DP)
        -------------------------
        - Stores results of subproblems to avoid redundant calculations.
        
        Recurrence Relation:
        maxMoney(i) = max(maxMoney(i-1), nums[i] + maxMoney(i-2))

        Time Complexity: O(n)
        Space Complexity: O(n) - Due to recursion depth and memo storage
        """
        memo = {}

        def helper(i):
            if i < 0:
                return 0
            if i in memo:
                return memo[i]  # Return cached result
            
            memo[i] = max(helper(i - 1), nums[i] + helper(i - 2))
            return memo[i]

        return helper(len(nums) - 1)

    
    def rob_dp(self, nums: List[int]) -> int:
        """
        Bottom-Up DP (Tabulation)
        -------------------------
        - Uses an array to store subproblem solutions.
        
        Recurrence Relation:
        dp[i] = max(dp[i-1], nums[i] + dp[i-2])
        
        Time Complexity: O(n)
        Space Complexity: O(n) - Uses DP array
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        dp = [0] * len(nums)  # Create DP array
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])  # Initialize base cases

        for i in range(2, len(nums)):  # Compute dp[i] iteratively
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])

        return dp[-1]  # The last element contains the answer

    
    def rob(self, nums: List[int]) -> int:
        """
        Optimized DP (O(1) Space)
        -------------------------
        - Instead of using an array, we only store the last two values.
        
        Recurrence Relation:
        maxMoney(i) = max(maxMoney(i-1), nums[i] + maxMoney(i-2))
        
        Time Complexity: O(n)
        Space Complexity: O(1) - Uses only two variables
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        prev1, prev2 = max(nums[0], nums[1]), nums[0]  # Equivalent to dp[1] and dp[0]

        for i in range(2, len(nums)):  # Iterate over the array
            current = max(prev1, nums[i] + prev2)  # Recurrence relation
            prev2, prev1 = prev1, current  # Update previous values

        return prev1
            