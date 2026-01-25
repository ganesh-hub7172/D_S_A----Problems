class Solution:
    def kLengthApart(self, nums, k):
        last_one_index = -1  # No 1 seen yet
        
        for i, num in enumerate(nums):
            if num == 1:
                if last_one_index != -1 and i - last_one_index - 1 < k:
                    return False
                last_one_index = i
        
        return True
