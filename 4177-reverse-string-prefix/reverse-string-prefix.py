class Solution:
    def reversePrefix(self, s, k):
        # Reverse the first k characters and concatenate with the rest
        return s[:k][::-1] + s[k:]
