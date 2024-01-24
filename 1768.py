class Solution(object):
    def mergeAlternately(self, word1, word2):
        self = []
        i = j = 0
        while i < len(word1) or j < len(word2):
            if i < len(word1):
                self.append(word1[i])
                i += 1
            if j < len(word2):
                self.append(word2[j])
                j += 1
        return ''.join(self)        