class Solution:
    """
    nums = [1,5,4,2,9,9,9], k = 3
    1,5,4 -> 5,4,2, -> 4,2,9 -> 2,9,9

    at left 0, right is at 2
    """
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        seen_numbers = set()
        left = 0
        max_sum = 0
        current_sum = 0

        for right in range(len(nums)):
            while nums[right] in seen_numbers:
                seen_numbers.remove(nums[left])
                current_sum = 0


            current_sum += nums[right]

            if right - left + 1 == k:
                max_sum = max(current_sum, max_sum)
                left +=1


from functools import lru_cache

def get_lexi_smallest_sequence(word1, word2):
    n, m = len(word1), len(word2)

    @lru_cache(None)  # Memoization to optimize repeated calls
    def helper(ix1, ix2, can_change):
        # Base cases
        if ix2 < 0:  # Successfully matched all of word2
            return []
        if ix1 < 0:  # Ran out of characters in word1 before matching word2
            return None

        # Option 1: Match the current character
        if word1[ix1] == word2[ix2]:
            res = helper(ix1 - 1, ix2 - 1, can_change)
            if res is not None:
                return res + [ix1]

        # Option 2: Allow one mismatch (if not already used)
        if can_change > 0:
            res = helper(ix1 - 1, ix2 - 1, can_change - 1)
            if res is not None:
                return res + [ix1]

        # Option 3: Skip current character in word1 to maintain lexicographical order
        return helper(ix1 - 1, ix2, can_change)

    # Start recursion from the last indices
    result = helper(n - 1, m - 1, 1)  # Allow at most 1 change

    return result if result is not None else []    



        

                



