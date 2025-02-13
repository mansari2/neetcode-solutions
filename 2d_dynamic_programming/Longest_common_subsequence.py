"""
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

 

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
"""
from functools import cache
from typing import List

class Solution:
    """
    A class that implements different solutions to the Longest Common Subsequence (LCS) problem.
    """

    def lcs_brute_force(self, text1: str, text2: str) -> int:
        """
        Brute Force Recursion (Exponential)
        ------------------------------------
        Recurrence Relation:
        - If characters match: LCS(i, j) = 1 + LCS(i + 1, j + 1)
        - Otherwise: LCS(i, j) = max(LCS(i + 1, j), LCS(i, j + 1))
        
        Time Complexity: O(2^(m+n)) - Exponential due to recursion branching.
        Space Complexity: O(m + n) - Recursion stack depth.
        """
        def dp(i, j):
            if i == len(text1) or j == len(text2):  # Base case: End of either string
                return 0

            if text1[i] == text2[j]:  # If characters match, count +1 and move both pointers
                return 1 + dp(i + 1, j + 1)

            # Otherwise, take max of either skipping i or j
            return max(dp(i + 1, j), dp(i, j + 1))

        return dp(0, 0)

    def lcs_memoization(self, text1: str, text2: str) -> int:
        """
        Memoization (Top-Down DP)
        -------------------------
        Recurrence Relation:
        - If characters match: LCS(i, j) = 1 + LCS(i + 1, j + 1)
        - Otherwise: LCS(i, j) = max(LCS(i + 1, j), LCS(i, j + 1))
        
        Time Complexity: O(m × n)
        Space Complexity: O(m × n) - Due to recursion depth and memoization table.
        """
        @cache  # Cache results to avoid redundant recursive calls
        def dp(i, j):
            if i == len(text1) or j == len(text2):  # Base case
                return 0

            if text1[i] == text2[j]:  # If characters match
                return 1 + dp(i + 1, j + 1)

            return max(dp(i + 1, j), dp(i, j + 1))

        return dp(0, 0)


    def lcs_tabulation(self, text1: str, text2: str) -> int:
        """
        Bottom-Up DP (Tabulation) - Filling in Natural Order
        ----------------------------------------------------
        Recurrence Relation:
        - If characters match: dp[i][j] = 1 + dp[i-1][j-1]
        - Otherwise: dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        Time Complexity: O(m × n)
        Space Complexity: O(m × n)
        """
        m, n = len(text1), len(text2)

        # Create DP table initialized to 0
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Fill the table in normal order (top-left to bottom-right)
        for i in range(1, m + 1):  # Iterate over text1
            for j in range(1, n + 1):  # Iterate over text2
                if text1[i - 1] == text2[j - 1]:  # If characters match
                    dp[i][j] = 1 + dp[i - 1][j - 1] # i-1, j-1 have the lcs for previous idx
                else:  # Otherwise, take the maximum LCS found so far
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) #either lcs 

        return dp[m][n]  # LCS length is stored at the bottom-right cell


    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        Space-Optimized DP (1D Array) - Filling in Natural Order
        --------------------------------------------------------
        Recurrence Relation:
        - If characters match: curr[j] = 1 + prev[j-1]
        - Otherwise: curr[j] = max(prev[j], curr[j-1])
        
        Time Complexity: O(m × n)
        Space Complexity: O(n) - Uses only two 1D arrays.
        """
        m, n = len(text1), len(text2)
        prev = [0] * (n + 1)  # Previous row

        for i in range(1, m + 1):  # Iterate over text1
            curr = [0] * (n + 1)  # Current row being processed
            for j in range(1, n + 1):  # Iterate over text2
                if text1[i - 1] == text2[j - 1]:  # If characters match
                    curr[j] = 1 + prev[j - 1]
                else:
                    curr[j] = max(prev[j], curr[j - 1])
            prev = curr  # Move current row to previous row

        return prev[n]