class Solution:
    def isPalindrome(self, s):
        cleaned = []
        
        for ch in s:
            if ch.isalnum():
                cleaned.append(ch.lower())
        
        return cleaned == cleaned[::-1]
