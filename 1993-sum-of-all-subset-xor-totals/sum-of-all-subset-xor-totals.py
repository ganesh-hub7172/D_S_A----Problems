class Solution:
    def subsetXORSum(self, nums):
        def dfs(index, current_xor):
            if index == len(nums):
                return current_xor
            # Include nums[index]
            include = dfs(index + 1, current_xor ^ nums[index])
            # Exclude nums[index]
            exclude = dfs(index + 1, current_xor)
            return include + exclude
        
        return dfs(0, 0)

# Example usage:
nums = [1, 3]
ret = Solution().subsetXORSum(nums)
print(ret)  # Output: 6
