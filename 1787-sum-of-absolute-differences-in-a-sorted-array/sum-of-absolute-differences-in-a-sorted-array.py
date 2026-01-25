class Solution:
    def getSumAbsoluteDifferences(self, nums):
        n = len(nums)
        prefix = [0] * n
        
        # Build prefix sum
        for i in range(1, n):
            prefix[i] = prefix[i - 1] + nums[i - 1]
        
        total = sum(nums)
        result = [0] * n
        
        for i in range(n):
            left_sum = nums[i] * i - prefix[i]
            right_sum = (total - prefix[i] - nums[i]) - nums[i] * (n - i - 1)
            result[i] = left_sum + right_sum
        
        return result
