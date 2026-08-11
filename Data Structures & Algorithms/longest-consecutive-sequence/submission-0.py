class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Convert the array to a Hash Set for O(1) lookups
        num_set = set(nums)
        longest_streak = 0
        
        for num in num_set:
            # Check if this number is the start of a sequence
            # (i.e., the number before it is NOT in the set)
            if (num - 1) not in num_set:
                current_num = num
                current_streak = 1
                
                # Count upwards as long as the sequence continues
                while (current_num + 1) in num_set:
                    current_num += 1
                    current_streak += 1
                    
                # Update our maximum streak
                longest_streak = max(longest_streak, current_streak)
                
        return longest_streak