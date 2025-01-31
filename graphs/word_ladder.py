# leetcode link : https://leetcode.com/problems/word-ladder/
from collections import deque
from typing import List
from string import ascii_letters

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """ we want to find the shortest transformation sequence from beginWord to endWord. we add the list of words to the set
        we can add the first word along with the level to the queue. we can then iterate over the word and change each character
        and check if the new word is in the wordlist. if it is we can add it to the queue and increment the level. we can keep track"""
        wordlist = set(wordList)  # Convert list to set for O(1) lookups
        if endWord not in wordlist:  
            return 0  # If endWord is not in the wordList, no transformation is possible
        
        queue = deque([(beginWord, 1)])  # BFS queue stores (current_word, transformation_steps)
        visited = {beginWord}  # Track visited words to prevent cycles
        
        while queue:
            word, level = queue.popleft()  # Get current word and number of transformations so far
            
            if word == endWord:
                return level  # If we reach endWord, return the number of transformations
            
            for i in range(len(word)):  # Try changing each character in the word
                for letter in ascii_letters:  # Replace with every possible letter
                    newWord = word[:i] + letter + word[i+1:]  # Form a new word
                    
                    if newWord not in visited and newWord in wordlist:  
                        queue.append((newWord, level + 1))  # Add to queue with incremented level
                        visited.add(newWord)  # Mark the word as visited
        
        return 0  # If we exit the loop without finding endWord, return 0 (no valid transformation)
    
"""
time complexity : O(M^2 * N) where M is the length of each word and N is the total number of words in the input word list.
space complexity : O(M^2 * N)
"""

from collections import deque

class Solution2:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        1. Bi-directional BFS (Optimized BFS)
Instead of searching from beginWord to endWord, we search from both ends simultaneously."""
        wordlist = set(wordList)
        if endWord not in wordlist:
            return 0
        
        forward_queue = {beginWord}  # BFS from start
        backward_queue = {endWord}  # BFS from end
        visited = set()
        level = 1
        
        while forward_queue and backward_queue:
            if len(forward_queue) > len(backward_queue):
                forward_queue, backward_queue = backward_queue, forward_queue  # Expand the smaller queue
            
            next_queue = set()
            for word in forward_queue:
                for i in range(len(word)):
                    for char in 'abcdefghijklmnopqrstuvwxyz':
                        newWord = word[:i] + char + word[i+1:]
                        
                        if newWord in backward_queue:
                            return level + 1  # If the two searches meet, return transformation count
                        
                        if newWord in wordlist and newWord not in visited:
                            next_queue.add(newWord)
                            visited.add(newWord)
            
            forward_queue = next_queue
            level += 1  # Increment transformation level
        
        return 0  # No valid transformation sequence found
    
    """
    time complexity : O(M^2 * N) where M is the length of each word and N is the total number of words in the input word list.
    space complexity : O(M^2 * N)
    """

