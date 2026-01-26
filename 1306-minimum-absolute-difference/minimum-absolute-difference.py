class Solution:
    def minimumAbsDifference(self, arr):
        arr.sort()
        
        min_diff = float('inf')
        result = []
        
        # Find minimum difference
        for i in range(1, len(arr)):
            min_diff = min(min_diff, arr[i] - arr[i - 1])
        
        # Collect pairs with minimum difference
        for i in range(1, len(arr)):
            if arr[i] - arr[i - 1] == min_diff:
                result.append([arr[i - 1], arr[i]])
        
        return result
