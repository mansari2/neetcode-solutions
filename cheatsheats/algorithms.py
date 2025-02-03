"""
Common Algorithm Templates for LeetCode Problems

This file contains commonly used algorithm structures in Python.
Each section includes a brief description and a LeetCode example.
"""

# Two Pointers: One Input, Opposite Ends (e.g., LeetCode 125 - Valid Palindrome)
def two_pointers_opposite_ends(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        # Example: if arr[left] == arr[right]: do something
        if CONDITION:
            left += 1
        else:
            right -= 1
    
    return # return value

# Two Pointers: Two Inputs, Exhaust Both (e.g., LeetCode 88 - Merge Sorted Array)
def two_pointers_two_inputs(arr1, arr2):
    i = j = 0

    while i < len(arr1) and j < len(arr2):
        # Example: if arr1[i] < arr2[j]: do something
        if CONDITION:
            i += 1
        else:
            j += 1
    while i < len(arr1):
        i += 1
    while j < len(arr2):
        j += 1

    return # return value

# Sliding Window (e.g., LeetCode 3 - Longest Substring Without Repeating Characters)
def sliding_window(arr):
    left = curr = ans = 0

    for right in range(len(arr)):
        # Add arr[right] to curr
        
        while WINDOW_CONDITION_BROKEN:
            # Remove arr[left] from curr
            left += 1

        # Update ans

    return ans

# Prefix Sum (e.g., LeetCode 560 - Subarray Sum Equals K)
def prefix_sum(arr):
    prefix_sums = [0] * (len(arr) + 1)

    for i in range(len(arr)):
        prefix_sums[i + 1] = prefix_sums[i] + arr[i]
    
    return prefix_sums

# Binary Search (e.g., LeetCode 704 - Binary Search)
def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
# Binary search: duplicate elements, left-most insertion point (e.g., LeetCode 35 - Search Insert Position)
def fn(arr, target):
    left = 0
    right = len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] >= target:
            right = mid
        else:
            left = mid + 1

    return left

# Binary search: duplicate elements, right-most insertion point (e.g., LeetCode 34 - Find First and Last Position of Element in Sorted Array)
def fn(arr, target):
    left = 0
    right = len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] > target:
            right = mid
        else:
            left = mid + 1

    return left

# Binary search: for greedy problems (e.g., LeetCode 1011 - Capacity To Ship Packages Within D Days)
def fn_min(arr):
    def check(x):
        # this function is implemented depending on the problem
        return BOOLEAN

    left = MINIMUM_POSSIBLE_ANSWER
    right = MAXIMUM_POSSIBLE_ANSWER
    while left <= right:
        mid = (left + right) // 2
        if check(mid):
            right = mid - 1
        else:
            left = mid + 1
    
    return left
# Binary search: for greedy problems looking for max
def fn_max(arr):
    def check(x):
        # this function is implemented depending on the problem
        return BOOLEAN

    left = MINIMUM_POSSIBLE_ANSWER
    right = MAXIMUM_POSSIBLE_ANSWER
    while left <= right:
        mid = (left + right) // 2
        if check(mid):
            left = mid + 1
        else:
            right = mid - 1
    
    return right
# Efficient String Building (e.g., LeetCode 271 - Encode and Decode Strings)
def efficient_string_building(strings):
    return "".join(strings)  # Faster than += in Python
# another example arr is a list of characters
def fn(arr):
    ans = []
    for c in arr:
        ans.append(c)
    
    return "".join(ans)

# Fast and Slow Pointers (e.g., LeetCode 141 - Linked List Cycle)
def fast_slow_pointers(head):
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True

    return False

# Reverse a Linked List (e.g., LeetCode 206 - Reverse Linked List)
def reverse_linked_list(head):
    prev = None
    curr = head

    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    return prev

# Find number of subarrays that fit an exact criteria (e.g., LeetCode 930 - Binary Subarrays With Sum)
from collections import defaultdict

def fn(arr, k):
    counts = defaultdict(int)
    counts[0] = 1
    ans = curr = 0

    for num in arr:
        # do logic to change curr
        ans += counts[curr - k]
        counts[curr] += 1
    
    return ans

# Monotonic Increasing Stack (e.g., LeetCode 739 - Daily Temperatures)
def monotonic_stack(arr):
    stack = []
    result = [0] * len(arr)

    for i, num in enumerate(arr):
        while stack and stack[-1] < num:
            stack.pop()
        stack.append(num)

    return result

# Binary tree: DFS recursive (e.g., LeetCode 104 - Maximum Depth of Binary Tree)
def dfs(root):
    if not root:
        return
    
    ans = 0

    # do logic
    dfs(root.left)
    dfs(root.right)
    return ans

# Binary tree: DFS iterative (e.g., LeetCode 104 - Maximum Depth of Binary Tree)
def dfs(root):
    stack = [root]
    ans = 0

    while stack:
        node = stack.pop()
        # do logic
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)

    return ans

# Binary tree: BFS (e.g., LeetCode 102 - Binary Tree Level Order Traversal)
from collections import deque

def fn(root):
    queue = deque([root])
    ans = 0

    while queue:
        current_length = len(queue)
        # do logic for current level

        for _ in range(current_length):
            node = queue.popleft()
            # do logic
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return ans

# For the graph templates, assume the nodes are numbered from 0 to n - 1 and the graph is given as an adjacency list. 
# Depending on the problem, you may need to convert the input into an equivalent adjacency list before using the templates.

# Graph DFS recursive (e.g., LeetCode 200 - Number of Islands)
def fn(graph):
    def dfs(node):
        ans = 0
        # do some logic
        for neighbor in graph[node]:
            if neighbor not in seen:
                seen.add(neighbor)
                ans += dfs(neighbor)
        
        return ans

    seen = {START_NODE}
    return dfs(START_NODE)
# Graph DFS iterative (e.g., LeetCode 200 - Number of Islands)
def fn(graph):
    stack = [START_NODE]
    seen = {START_NODE}
    ans = 0

    while stack:
        node = stack.pop()
        # do some logic
        for neighbor in graph[node]:
            if neighbor not in seen:
                seen.add(neighbor)
                stack.append(neighbor)
    
    return ans

# Graph BFS (e.g., LeetCode 127 - Word Ladder)
from collections import deque

def bfs(graph, start):
    queue = deque([start])
    visited = set([start])

    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return visited

# Dijkstra's Algorithm for Shortest Path
# Time Complexity: O((V + E) log V) where V is the number of vertices and E is the number of edges
# Space Complexity: O(V)
def dijkstra(graph, start):
    import heapq
    heap = [(0, start)]
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    while heap:
        cost, node = heapq.heappop(heap)
        if cost > distances[node]:
            continue

        for neighbor, weight in graph[node]:
            new_cost = cost + weight
            if new_cost < distances[neighbor]:
                distances[neighbor] = new_cost
                heapq.heappush(heap, (new_cost, neighbor))

    return distances

# Dynamic programming: top-down memoization (e.g., LeetCode 70 - Climbing Stairs)
# Time Complexity: O(n) where n is the size of the input
# Space Complexity: O(n) for the memoization table
def fn(arr):
    def dp(STATE):
        if BASE_CASE:
            return 0
        
        if STATE in memo:
            return memo[STATE]
        
        ans = RECURRENCE_RELATION(STATE)
        memo[STATE] = ans
        return ans

    memo = {}
    return dp(STATE_FOR_WHOLE_INPUT)

# Example for Climbing Stairs
# Time Complexity: O(n)
# Space Complexity: O(n)
def climbStairs(n):
    def dp(i):
        if i <= 1:
            return 1
        if i in memo:
            return memo[i]
        memo[i] = dp(i - 1) + dp(i - 2)
        return memo[i]

    memo = {}
    return dp(n)

# Backtracking (e.g., LeetCode 46 - Permutations)
# Time Complexity: O(n * n!) where n is the length of the input
# Space Complexity: O(n) for the recursion stack
def backtrack(curr, args):
    if BASE_CASE:
        # modify the answer
        return
    
    ans = 0
    for ITERATE_OVER_INPUT:
        # modify the current state
        ans += backtrack(curr, args)
        # undo the modification of the current state
    
    return ans

# Example for Permutations
# Time Complexity: O(n * n!)
# Space Complexity: O(n)
def permute(nums):
    def backtrack(first=0):
        if first == n:
            output.append(nums[:])
        for i in range(first, n):
            nums[first], nums[i] = nums[i], nums[first]
            backtrack(first + 1)
            nums[first], nums[i] = nums[i], nums[first]

    n = len(nums)
    output = []
    backtrack()
    return output
