from collections import defaultdict

class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []

        parents = defaultdict(list)
        level = set([beginWord])
        found = False

        while level and not found:
            next_level = set()

            for word in level:
                if word in wordSet:
                    wordSet.remove(word)

            for word in level:
                for i in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        new_word = word[:i] + c + word[i+1:]
                        if new_word in wordSet:
                            parents[new_word].append(word)
                            next_level.add(new_word)
                            if new_word == endWord:
                                found = True

            level = next_level

        res = []

        def backtrack(word, path):
            if word == beginWord:
                res.append(path[::-1])
                return
            for p in parents[word]:
                backtrack(p, path + [p])

        if found:
            backtrack(endWord, [endWord])

        return res
