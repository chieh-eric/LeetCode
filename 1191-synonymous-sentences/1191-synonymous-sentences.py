from collections import defaultdict
class UnionFind():
    def __init__(self):
        self.parent = {}

    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x

        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, x, y):
        self.parent[self.find(x)] = self.find(y)

class Solution(object):
    def generateSentences(self, synonyms, text):
        """
        :type synonyms: List[List[str]]
        :type text: str
        :rtype: List[str]
        """
        n = UnionFind()
        for i, j in synonyms:
            n.union(i,j)
        
        group = defaultdict(set)
        for word in n.parent:
            root = n.find(word)
            group[root].add(word)
        for key in group:
            group[key] = sorted(group[key])
        
        res = []
        words = text.split(" ")
        m = len(words)

        def backtrack(cur,index):

            if index == m:
                res.append(" ".join(cur))
                return
            
            word = words[index]
            
            choices = []
            if word in n.parent:
                choices = group[n.find(word)]
            else:
                choices = [word]

            for choice in choices:
                cur.append(choice)
                backtrack(cur,index+1)
                cur.pop()

        backtrack([],0)
        return res