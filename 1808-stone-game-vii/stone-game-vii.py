class Solution:
    def stoneGameVII(self, stones):
        n = len(stones)

        # Prefix sum for quick range sum
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stones[i]

        def get_sum(i, j):
            return prefix[j + 1] - prefix[i]

        # dp[i][j] = max score difference from stones[i..j]
        dp = [[0] * n for _ in range(n)]

        # Length from 2 to n
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                remove_left = get_sum(i + 1, j) - dp[i + 1][j]
                remove_right = get_sum(i, j - 1) - dp[i][j - 1]

                dp[i][j] = max(remove_left, remove_right)

        return dp[0][n - 1]
