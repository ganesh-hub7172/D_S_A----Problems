class Solution:
    def wordBreak(self, s, wordDict):
        wordSet = set(wordDict)
        memo = {}

        def dfs(sub):
            if sub in memo:
                return memo[sub]

            if not sub:
                return [""]

            res = []
            for word in wordSet:
                if sub.startswith(word):
                    rest_sentences = dfs(sub[len(word):])
                    for sentence in rest_sentences:
                        if sentence:
                            res.append(word + " " + sentence)
                        else:
                            res.append(word)

            memo[sub] = res
            return res

        return dfs(s)
