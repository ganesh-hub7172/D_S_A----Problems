class Solution:
    def minPairSum(self, nums):
        nums.sort()
        left = 0
        right = len(nums) - 1
        max_sum = 0
        
        while left < right:
            max_sum = max(max_sum, nums[left] + nums[right])
            left += 1
            right -= 1
        
        return max_sum
