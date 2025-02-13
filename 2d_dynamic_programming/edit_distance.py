"""
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character
 

Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')

"""
from functools import cache

class Solution:
    """
    A class that implements different solutions for the Edit Distance (Levenshtein Distance) problem.
    """

    def edit_distance_brute_force(self, word1: str, word2: str) -> int:
        """
        Brute Force Recursion (Exponential)
        ------------------------------------
        Recurrence Relation:
        - If characters match: Edit(i, j) = Edit(i-1, j-1)
        - Otherwise: Edit(i, j) = min(
              Edit(i-1, j) + 1   # Deletion
              Edit(i, j-1) + 1   # Insertion
              Edit(i-1, j-1) + 1 # Replacement
          )
        
        Time Complexity: O(3^max(m, n)) - Exponential due to recursion branching.
        Space Complexity: O(m + n) - Recursion stack depth.
        """
        def dp(i, j):
            if i == 0: return j  # Base case: Insert all remaining characters
            if j == 0: return i  # Base case: Delete all remaining characters
            
            if word1[i - 1] == word2[j - 1]:  # If characters match
                return dp(i - 1, j - 1)

            return min(
                dp(i - 1, j) + 1,   # Delete
                dp(i, j - 1) + 1,   # Insert
                dp(i - 1, j - 1) + 1 # Replace
            )

        return dp(len(word1), len(word2))


    def edit_distance_memoization(self, word1: str, word2: str) -> int:
        """
        Memoization (Top-Down DP)
        -------------------------
        Recurrence Relation:
        - If characters match: Edit(i, j) = Edit(i-1, j-1)
        - Otherwise: Edit(i, j) = min(
              Edit(i-1, j) + 1   # Deletion
              Edit(i, j-1) + 1   # Insertion
              Edit(i-1, j-1) + 1 # Replacement
          )
        
        Time Complexity: O(m × n)
        Space Complexity: O(m × n) - Due to recursion depth and memoization table.
        """
        @cache  # Cache results to avoid redundant recursive calls
        def dp(i, j):
            if i == 0: return j  # Base case
            if j == 0: return i

            if word1[i - 1] == word2[j - 1]:  # If characters match
                return dp(i - 1, j - 1)

            return min(
                dp(i - 1, j) + 1,   # Delete
                dp(i, j - 1) + 1,   # Insert
                dp(i - 1, j - 1) + 1 # Replace
            )

        return dp(len(word1), len(word2))


    def edit_distance_tabulation(self, word1: str, word2: str) -> int:
        """
        Bottom-Up DP (Tabulation) - Filling in Natural Order
        ----------------------------------------------------
        Recurrence Relation:
        - If characters match: dp[i][j] = dp[i-1][j-1]
        - Otherwise: dp[i][j] = min(
              dp[i-1][j] + 1   # Deletion
              dp[i][j-1] + 1   # Insertion
              dp[i-1][j-1] + 1 # Replacement
          )
        
        Time Complexity: O(m × n)
        Space Complexity: O(m × n)
        """
        m, n = len(word1), len(word2)

        # Create DP table initialized to 0
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Base case: transforming empty string to non-empty string
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j

        # Fill the table in normal order (top-left to bottom-right)
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:  # If characters match
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(
                        dp[i - 1][j] + 1,  # Delete
                        dp[i][j - 1] + 1,  # Insert
                        dp[i - 1][j - 1] + 1 # Replace
                    )

        return dp[m][n]  # Edit distance is stored at the bottom-right cell


    def minDistance(self, word1: str, word2: str) -> int:
        """
        Space-Optimized DP (1D Array)
        --------------------------------------------------------
        Recurrence Relation:
        - If characters match: curr[j] = prev[j-1]
        - Otherwise: curr[j] = min(
              prev[j] + 1,  # Deletion
              curr[j-1] + 1,  # Insertion
              prev[j-1] + 1  # Replacement
          )
        
        Time Complexity: O(m × n)
        Space Complexity: O(n) - Uses only two 1D arrays.
        """
        m, n = len(word1), len(word2)
        prev = list(range(n + 1))  # Initialize first row

        for i in range(1, m + 1):
            curr = [0] * (n + 1)
            curr[0] = i  # Base case: transforming first `i` characters

            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:  # If characters match
                    curr[j] = prev[j - 1]
                else:
                    curr[j] = min(prev[j] + 1, curr[j - 1] + 1, prev[j - 1] + 1)

            prev = curr  # Move current row to previous row

        return prev[n]