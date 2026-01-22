class Solution:
    def minCut(self, s):
        n = len(s)

        # palindrome table
        isPal = [[False] * n for _ in range(n)]

        for i in range(n):
            isPal[i][i] = True

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    if length == 2:
                        isPal[i][j] = True
                    else:
                        isPal[i][j] = isPal[i + 1][j - 1]

        # dp array
        dp = [0] * n

        for i in range(n):
            if isPal[0][i]:
                dp[i] = 0
            else:
                dp[i] = float('inf')
                for j in range(1, i + 1):
                    if isPal[j][i]:
                        dp[i] = min(dp[i], dp[j - 1] + 1)

        return dp[n - 1]
