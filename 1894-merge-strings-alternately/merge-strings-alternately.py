class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        comb=[]
        for i in range(min(len(word1),len(word2))):
            comb.append(word1[i]+word2[i])
            
        comb.append(word1[len(word2):])
        comb.append(word2[len(word1):])

        return "".join(comb)
