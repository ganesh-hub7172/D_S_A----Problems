class Solution:
    def reverseWords(self, s):
        words = s.split()          # removes extra spaces automatically
        words.reverse()            # reverse the words
        return " ".join(words)     # join with single space
