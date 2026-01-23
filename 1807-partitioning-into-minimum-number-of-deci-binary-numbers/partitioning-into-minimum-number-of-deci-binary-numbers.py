class Solution:
    def minPartitions(self, n):
        # Convert each character to int and return the max
        return max(int(ch) for ch in n)
