class Solution:
    def getSneakyNumbers(self, nums):
        from collections import Counter
        count = Counter(nums)
        # Extract numbers that appear more than once
        return [num for num in count if count[num] > 1]

# Example usage:
nums = [0, 1, 1, 0]
ret = Solution().getSneakyNumbers(nums)
print(ret)  # Output: [0, 1]
