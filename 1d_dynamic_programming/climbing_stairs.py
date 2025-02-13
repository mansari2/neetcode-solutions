'''
Question: https//leetcode.com/problems/climbing-stairs/
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. 
In how many distinct ways can you climb to the top?
Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
'''

from typing import List

class Solution:
    def climbStairs_brute_force(self, n: int) -> int:
        """
        Brute Force: Recursively compute the number of ways to climb `n` steps.
        Time Complexity: O(2^n) - Exponential (TLE for large n)
        Space Complexity: O(n) - Recursive call stack depth
        Recurrence Relation:
        - f(n) = f(n-1) + f(n-2)
        """
        if n == 0:
            return 1  # Base case: 1 way to stay at step 0
        if n < 0:
            return 0  # Invalid case: No way to climb negative steps

        return self.climbStairs_brute_force(n - 1) + self.climbStairs_brute_force(n - 2)

    def climbStairs(self, n: int) -> int:
        """
        DP with Tabulation (Bottom-Up Approach): 
        Uses an array to store results for subproblems.
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        if n == 1:
            return 1
        dp = [0] * (n + 1)  # Create an array for n steps
        dp[0] = 1  # Base case: 1 way to stay at step 0
        dp[1] = 1  # ✅ Corrected: Only 1 way to reach step 1
        
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]  # Use recurrence relation
        
        return dp[n]  # Return the number of ways to reach step n

    def climbStairs_optimized(self, n: int) -> int:
        """
        Space Optimized DP (Fibonacci Approach): 
        Instead of using an array, we only store the last two values.
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if n == 1:
            return 1

        prev1, prev2 = 1, 2  # Base cases
        for i in range(3, n + 1):
            current = prev1 + prev2  # f(n) = f(n-1) + f(n-2)
            prev1, prev2 = prev2, current  # Update previous values

        return prev2  # The last computed value is the answer
        
            