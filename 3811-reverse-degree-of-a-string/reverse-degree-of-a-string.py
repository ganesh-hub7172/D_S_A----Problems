class Solution:
    def reverseDegree(self, s):
        total = 0
        for i, ch in enumerate(s):
            pos_in_string = i + 1  # 1-indexed
            reversed_alpha_value = 26 - (ord(ch) - ord('a'))
            total += pos_in_string * reversed_alpha_value
        return total
