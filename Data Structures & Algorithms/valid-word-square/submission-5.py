class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        for i, w in enumerate(words):
            for j,letter in enumerate(w):
                if  j >= len(words) or len(words[j]) <= i :
                    return False
                if words[i][j] != words[j][i]:
                    return False
        return True 


