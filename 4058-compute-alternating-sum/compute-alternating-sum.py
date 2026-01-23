class Solution:
    def alternatingSum(self, nums):
        total = 0
        for i, num in enumerate(nums):
            if i % 2 == 0:  # even index
                total += num
            else:           # odd index
                total -= num
        return total
