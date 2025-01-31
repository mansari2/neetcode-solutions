"""
Question: https://leetcode.com/problems/container-with-most-water/
"""

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Use Two Pointers -> `left` and `right`, compare the volume of water held by each container and only
        move the pointer with the smaller height to get the most water in the next container.
        Also, keep track of the max volume of water held by any container.
        Walk through the problem to demonstrate the logic of why you want to increment or decrement the pointers.
        Initially, we consider the area constituting the exterior most lines. Now, to maximize the area, we need to consider the area between the lines of larger lengths.
        If we try to move the pointer at the longer line inwards, we won't gain any increase in area, since it is limited by the shorter line. But moving the shorter line's pointer could turn out to be beneficial, as per the same argument, despite the reduction in the width. 
        This is done since a relatively longer line obtained by moving the shorter line's pointer might overcome the reduction in area caused by the width reduction.

        Time Complexity: O(N)        
        """
        
        # Init the two pointers on opposite ends of the list `height`
        left_wall_index, right_wall_index = 0, len(height)-1
        most_water = 0
        
        # Iterate until thw two pointers cross over
        while left_wall_index < right_wall_index:
            
            # The max level of water the container can hold depends on the shortest height of the container
            # The max level of water can only be optimized by increasing the length of the smaller of the two n's 
            # i.e. min of height[left] or height[right]
            container_height = min(height[left_wall_index], height[right_wall_index])

            # Width of current container width will be dist b/w right and left i.e. `right - left`
            container_width = right_wall_index - left_wall_index
            
            # Now calculate the water held by current container i.e. calculate the area of container (rectangle)
            curr_water = container_height * container_width
            
            # Update max value of the `most_water` 
            most_water = max(most_water, curr_water)
            
            # Update the left and right pointers for the next iteration.
            # We remove the side with the smaller height (to get most water in the next container)
            # i.e. if 'left' height is less, we move left and vice-versa
            if height[left_wall_index] < height[right_wall_index]:
                left_wall_index += 1
            else:
                right_wall_index -= 1
                        
        return most_water
    