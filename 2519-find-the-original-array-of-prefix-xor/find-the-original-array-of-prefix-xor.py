class Solution:
    def findArray(self, pref):
        n = len(pref)
        arr = [0] * n

        arr[0] = pref[0]

        for i in range(1, n):
            arr[i] = pref[i] ^ pref[i - 1]

        return arr
