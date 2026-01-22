class Solution:
    def largestNumber(self, nums):
        # Convert numbers to strings
        nums = list(map(str, nums))
        
        # Custom sort using comparison
        nums.sort(key=lambda x: x*10, reverse=True)
        
        # Join the numbers
        result = ''.join(nums)
        
        # Handle leading zeros
        return '0' if result[0] == '0' else result
