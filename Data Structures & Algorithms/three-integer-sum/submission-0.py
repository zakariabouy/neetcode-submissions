class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        
        for i in range(n - 2):
            # Optimization: sorted, so if nums[i] > 0, no triplet can sum to 0
            if nums[i] > 0:
                break
            # Skip duplicate i values
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left, right = i + 1, n - 1
            target = -nums[i]
            
            while left < right:
                s = nums[left] + nums[right]
                if s == target:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    # Skip duplicate left values
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    # Skip duplicate right values
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif s < target:
                    left += 1
                else:
                    right -= 1
        
        return res