class Solution:
    def differenceOfSums(self, n, m):
        total = n * (n + 1) // 2
        k = n // m
        num2 = m * k * (k + 1) // 2
        return total - 2 * num2
