class Solution:
    def minimizeArrayValue(self, nums):
        max_val = 0
        prefix_sum = 0

        for i, num in enumerate(nums):
            prefix_sum += num
            # Ceiling of average
            avg = (prefix_sum + i) // (i + 1)
            max_val = max(max_val, avg)

        return max_val
