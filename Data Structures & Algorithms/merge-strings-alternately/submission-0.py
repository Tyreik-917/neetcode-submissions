class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n, m = len(word1), len(word2)
        i = j = 0
        word = ""

        while i < n and j < m:
            word += word1[i] + word2[j]

            i+=1
            j+=1

        return word + word1[i:] + word2[j:]