class Solution:
    def pivotArray(self, nums, pivot):
        less, equal, greater = [], [], []
        
        for num in nums:
            if num < pivot:
                less.append(num)
            elif num == pivot:
                equal.append(num)
            else:
                greater.append(num)
        
        # Combine the three lists
        return less + equal + greater

# Example usage
nums = [9,12,5,10,14,3,10]
pivot = 10
ret = Solution().pivotArray(nums, pivot)
print(ret)  # Output: [9, 5, 3, 10, 10, 12, 14]
