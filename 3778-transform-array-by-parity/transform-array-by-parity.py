class Solution:
    def transformArray(self, nums):
        # Step 1: Transform even → 0, odd → 1
        for i in range(len(nums)):
            nums[i] = 0 if nums[i] % 2 == 0 else 1
        
        # Step 2: Sort the array
        nums.sort()
        return nums
