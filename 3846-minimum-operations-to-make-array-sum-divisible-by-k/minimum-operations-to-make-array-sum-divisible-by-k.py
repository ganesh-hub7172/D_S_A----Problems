class Solution:
    def minOperations(self, nums, k):
        total = sum(nums)
        return total % k
