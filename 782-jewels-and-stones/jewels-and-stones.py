class Solution:
    def numJewelsInStones(self, jewels, stones):
        jewel_set = set(jewels)  # Make lookup O(1)
        count = 0
        for stone in stones:
            if stone in jewel_set:
                count += 1
        return count
