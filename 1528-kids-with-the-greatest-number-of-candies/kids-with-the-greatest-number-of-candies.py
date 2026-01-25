class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        max_candies = max(candies)
        result = []

        for c in candies:
            if c + extraCandies >= max_candies:
                result.append(True)
            else:
                result.append(False)

        return result
