from collections import deque

class Solution:
    def longestSubarray(self, nums, limit):
        max_deque = deque()  # stores elements in decreasing order
        min_deque = deque()  # stores elements in increasing order
        left = 0
        result = 0

        for right, num in enumerate(nums):
            # Maintain max deque
            while max_deque and num > max_deque[-1]:
                max_deque.pop()
            max_deque.append(num)

            # Maintain min deque
            while min_deque and num < min_deque[-1]:
                min_deque.pop()
            min_deque.append(num)

            # Shrink window if difference exceeds limit
            while max_deque[0] - min_deque[0] > limit:
                if nums[left] == max_deque[0]:
                    max_deque.popleft()
                if nums[left] == min_deque[0]:
                    min_deque.popleft()
                left += 1

            # Update result
            result = max(result, right - left + 1)

        return result
