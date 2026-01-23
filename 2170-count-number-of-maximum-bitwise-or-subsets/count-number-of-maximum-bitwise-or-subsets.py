class Solution:
    def countMaxOrSubsets(self, nums):
        self.max_or = 0
        self.count = 0
        
        # First compute the maximum possible OR of all elements
        for num in nums:
            self.max_or |= num
        
        def dfs(index, current_or):
            if index == len(nums):
                if current_or == self.max_or:
                    self.count += 1
                return
            # Option 1: Include nums[index] in subset
            dfs(index + 1, current_or | nums[index])
            # Option 2: Exclude nums[index] from subset
            dfs(index + 1, current_or)
        
        dfs(0, 0)
        return self.count
