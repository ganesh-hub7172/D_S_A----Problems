class Solution:
    def wordBreak(self, s, wordDict):
        wordSet = set(wordDict)
        memo = {}

        def dfs(sub):
            if sub in memo:
                return memo[sub]

            res = []
            if not sub:
                return [""]

            for word in wordSet:
                if sub.startswith(word):
                    rest = dfs(sub[len(word):])
                    for r in rest:
                        res.append(word + (" " + r if r else ""))

            memo[sub] = res
            return res

        return dfs(s)
