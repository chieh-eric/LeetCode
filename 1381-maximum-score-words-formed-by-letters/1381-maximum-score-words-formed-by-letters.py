from collections import defaultdict
class Solution(object):
    def maxScoreWords(self, words, letters, score):
        """
        :type words: List[str]
        :type letters: List[str]
        :type score: List[int]
        :rtype: int
        """
        frequency = defaultdict(int)
        cur_selected = defaultdict(int)

        for ch in letters:
            frequency[ch] += 1

        n = len(words)
        self.selected = []
        self.max_score = 0

        def backtrack(i):
            cur_score = 0
            if i == len(words):
                for word in self.selected:
                    for ch in word:
                        cur_score += score[ord(ch)-ord('a')]
                self.max_score = max(self.max_score, cur_score)
                return 
            
            for j in range(2):
                
                if j == 0:
                    for ch in words[i]:
                        cur_selected[ch] += 1
                    if all( frequency[key] >= cur_selected[key] for key in cur_selected):
                        self.selected.append(words[i])
                        backtrack(i+1)
                        self.selected.pop()
                    for ch in words[i]:
                        cur_selected[ch] -= 1

                    
                else:
                    backtrack(i+1)
        backtrack(0)
        return self.max_score