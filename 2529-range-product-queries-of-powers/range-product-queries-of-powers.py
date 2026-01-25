class Solution:
    def productQueries(self, n, queries):
        MOD = 10**9 + 7

        # Step 1: Build powers array
        powers = []
        bit = 1
        while n > 0:
            if n & 1:
                powers.append(bit)
            bit <<= 1
            n >>= 1

        # Step 2: Prefix product
        prefix = [1] * (len(powers) + 1)
        for i in range(len(powers)):
            prefix[i + 1] = (prefix[i] * powers[i]) % MOD

        # Step 3: Answer queries
        result = []
        for left, right in queries:
            product = prefix[right + 1] * pow(prefix[left], MOD - 2, MOD)
            result.append(product % MOD)

        return result
