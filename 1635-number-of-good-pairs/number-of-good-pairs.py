class Solution:
    def numIdenticalPairs(self, nums):
        from collections import defaultdict
        count = defaultdict(int)
        res = 0
        for num in nums:
            res += count[num]   # All previous occurrences form good pairs
            count[num] += 1
        return res

# Example usage
nums = [1,2,3,1,1,3]
ret = Solution().numIdenticalPairs(nums)
print(ret)  # Output: 4
