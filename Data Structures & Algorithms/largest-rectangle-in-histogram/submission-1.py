class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []  # (index, height)
        for i, h in enumerate(heights):
            start = i
            # If the current bar is shorter than the bar at the top of the stack,
            # we found a bottleneck. It's time to pop and calculate area.
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                
                # Formula: min_of_them (height) * len_of_them (current index - start index)
                max_area = max(max_area, height * (i - index))
                
                # The "Magic Trick": The current shorter bar extends backward 
                # into the space of the taller bar we just popped, so it steals its index.
                start = index
                
            # Push the current bar onto the stack with its original or stolen index
            stack.append((start, h))

        # At the end of the array, calculate the area for any bars left in the stack.
        # Since nothing blocked them, they extend all the way to the end of the array.
        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))

        return max_area