from math import comb
from typing import List

class Solution:
    """
    A class that contains different solutions to solve the 'Unique Paths' problem.
    """

    def unique_paths_brute_force(self, m: int, n: int) -> int:
        """
        Brute Force Recursion (Exponential)
        ------------------------------------
        Recurrence Relation:
        uniquePaths(m, n) = uniquePaths(m-1, n) + uniquePaths(m, n-1)

        Base Cases:
        - If m == 1 or n == 1: return 1 (Only one way to move)

        Time Complexity: O(2^(m+n)) - Exponential (TLE for large grids)
        Space Complexity: O(m + n) - Due to recursion depth
        """
        def helper(i, j):
            if i == 0 or j == 0:  # If at the top row or leftmost column, only one path exists
                return 1
            return helper(i - 1, j) + helper(i, j - 1)

        return helper(m - 1, n - 1)

    
    def unique_paths_memoization(self, m: int, n: int) -> int:
        """
        Memoization (Top-Down DP)
        -------------------------
        - Stores results of subproblems to avoid redundant calculations.

        Recurrence Relation:
        uniquePaths(m, n) = uniquePaths(m-1, n) + uniquePaths(m, n-1)

        Time Complexity: O(m * n)
        Space Complexity: O(m * n) - Due to memoization storage
        """
        memo = {}

        def helper(i, j):
            if i == 0 or j == 0:
                return 1
            if (i, j) in memo:
                return memo[(i, j)]  # Return cached result

            memo[(i, j)] = helper(i - 1, j) + helper(i, j - 1)
            return memo[(i, j)]

        return helper(m - 1, n - 1)

    
    def unique_paths_dp(self, m: int, n: int) -> int:
        """
        Bottom-Up DP (Tabulation)
        -------------------------
        - Uses a 2D DP table to store subproblem solutions.

        Recurrence Relation:
        dp[i][j] = dp[i-1][j] + dp[i][j-1]

        Time Complexity: O(m * n)
        Space Complexity: O(m * n) - Uses a DP array
        """
        dp = [[1] * n for _ in range(m)]  # Initialize grid with 1s

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]  # Compute unique paths

        return dp[-1][-1]  # Bottom-right cell contains the answer

    
    def uniquePaths(self, m: int, n: int) -> int:
        """
        Optimized DP (O(1) Space)
        -------------------------
        - Uses a 1D array instead of a 2D DP table.

        Recurrence Relation:
        dp[j] = dp[j] + dp[j-1]

        Time Complexity: O(m * n)
        Space Complexity: O(n) - Uses only one row

        """
        dp = [1] * n  # Initialize DP row with 1s

        for i in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j - 1]  # Update the current cell

        return dp[-1]  # Last cell contains the answer

    
    def unique_paths_combinatorial(self, m: int, n: int) -> int:
        """
        Combinatorial Solution
        ----------------------
        - The number of unique paths is equivalent to choosing (m-1) downward moves
          from a total of (m-1 + n-1) moves.

        Formula:
        C(m+n-2, m-1) = (m+n-2)! / [(m-1)! * (n-1)!]

        Time Complexity: O(m + n) - Factorial calculation
        Space Complexity: O(1) - No extra space used
        """
        return comb(m + n - 2, m - 1)


