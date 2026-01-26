class Solution:
    def minCut(self, s):
        n = len(s)
        
        # palindrome[i][j] = True if s[i:j+1] is palindrome
        palindrome = [[False] * n for _ in range(n)]
        
        for i in range(n):
            palindrome[i][i] = True
        
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    if length == 2 or palindrome[i + 1][j - 1]:
                        palindrome[i][j] = True

        dp = [0] * n
        
        for i in range(n):
            if palindrome[0][i]:
                dp[i] = 0
            else:
                dp[i] = i  # worst case: cut every character
                for j in range(i):
                    if palindrome[j + 1][i]:
                        dp[i] = min(dp[i], dp[j] + 1)

        return dp[-1]
