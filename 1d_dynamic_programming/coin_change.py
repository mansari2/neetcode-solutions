'''
Question: https://leetcode.com/problems/coin-change/
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

 

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0
'''

from typing import List
from collections import deque

class Solution:
    """
    A class that implements different solutions for the Coin Change problem.
    """

    def coinChange_brute_force(self, coins: List[int], amount: int) -> int:
        """
        Brute Force Recursion (Exponential)
        ------------------------------------
        - Try every possible way to form the amount by recursively subtracting each coin.
        - If the remaining amount is 0, we found a valid solution.
        - If the amount goes negative, it's an invalid path.
        
        Recurrence Relation:
        minCoins(amount) = 1 + min(minCoins(amount - c) for each c in coins)
        
        Time Complexity: O(2ⁿ) (TLE for large inputs)
        Space Complexity: O(n) (Recursion depth)
        """
        if amount == 0:
            return 0  # Base case: No coins needed
        if amount < 0:
            return float('inf')  # No valid solution

        min_coins = float('inf')

        for coin in coins:
            # Try using this coin and solve for the remaining amount
            res = self.coinChange_brute_force(coins, amount - coin)
            if res != float('inf'):  # If a solution exists, update min_coins
                min_coins = min(min_coins, res + 1)

        return min_coins if min_coins != float('inf') else -1  # Return -1 if no solution exists

    
    def coinChange_memoization(self, coins: List[int], amount: int) -> int:
        """
        Memoization (Top-Down DP)
        -------------------------
        - Uses a dictionary to store already computed results to avoid redundant calculations.
        - Recursively solve subproblems and store their solutions in `memo`.
        
        Recurrence Relation:
        minCoins(amount) = 1 + min(minCoins(amount - c) for each c in coins)
        
        Time Complexity: O(n × m) (Efficient for large inputs)
        Space Complexity: O(n) (Recursion stack + memo storage)
        """
        memo = {}

        def helper(amt):
            if amt == 0:
                return 0  # Base case: No coins needed
            if amt < 0:
                return float('inf')  # No valid solution
            if amt in memo:
                return memo[amt]  # Return cached result
            
            min_coins = float('inf')
            for coin in coins:
                res = helper(amt - coin)  # Recursive call for the remaining amount
                if res != float('inf'):
                    min_coins = min(min_coins, res + 1)

            memo[amt] = min_coins  # Store computed result
            return min_coins

        result = helper(amount)
        return result if result != float('inf') else -1  # Return -1 if no solution exists

    
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        Bottom-Up DP (Tabulation)
        -------------------------
        - Uses an array `dp` where dp[i] represents the minimum coins needed to make amount `i`.
        - Iteratively builds the solution for each amount from 1 to `amount`.

        Recurrence Relation:
        dp[i] = min(dp[i], 1 + dp[i - c]) for each coin c
        
        Steps:
        1. Create a DP table initialized with inf (since we need the minimum).
        2. Set `dp[0] = 0` because no coins are needed to make amount 0.
        3. Iterate through all amounts from 1 to `amount`, checking all coins.
        4. If the coin value is less than or equal to `i`, update `dp[i]`.
        5. Return `dp[amount]` if it has been updated; otherwise, return -1.

        Time Complexity: O(n × m) (Efficient for large inputs)
        Space Complexity: O(n) (Uses a DP table)
        """
        dp = [float('inf')] * (amount + 1)  # Initialize DP table
        dp[0] = 0  # Base case: 0 coins needed for amount 0

        for i in range(1, amount + 1):  # Iterate through each amount
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], dp[i - coin] + 1)  # Take the minimum number of coins

        return dp[amount] if dp[amount] != float('inf') else -1  # If dp[amount] is inf, return -1

    
    def coinChange_bfs(self, coins: List[int], amount: int) -> int:
        """
        Optimized BFS Approach
        -------------------------
        - Uses a queue to explore the shortest path (fewest number of coins).
        - This is equivalent to finding the shortest path in an unweighted graph.

        Steps:
        1. Initialize a queue with (remaining amount, steps taken).
        2. Use a set `visited` to avoid reprocessing the same amount.
        3. For each level in BFS, explore all coin possibilities.
        4. If `new_amt == 0`, return steps + 1 (we found the minimum coins needed).
        5. If `new_amt > 0` and not visited, add it to the queue.

        Time Complexity: O(n × m) (Efficient for large inputs)
        Space Complexity: O(n) (Uses a queue to track visited nodes)
        """
        if amount == 0:
            return 0  # No coins needed if amount is 0

        queue = deque([(amount, 0)])  # Queue holds (remaining amount, steps taken)
        visited = set()

        while queue:
            remaining, steps = queue.popleft()  # Dequeue the current amount

            for coin in coins:
                new_amt = remaining - coin  # Subtract coin from remaining amount
                if new_amt == 0:
                    return steps + 1  # Found the shortest path, return answer
                if new_amt > 0 and new_amt not in visited:
                    visited.add(new_amt)  # Mark as visited
                    queue.append((new_amt, steps + 1))  # Add new amount to queue

        return -1  # If no solution exists

