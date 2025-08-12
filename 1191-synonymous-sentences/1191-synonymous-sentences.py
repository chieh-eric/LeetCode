from collections import defaultdict
class UnionFind():
    def __init__(self):
        self.parent = {}
    
    def find(self,x):
        if x not in self.parent:
            self.parent[x] = x
            return x

        if self.parent[x] == x:
            return x
        
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self,x,y):
        px = self.find(x)
        py = self.find(y)

        self.parent[px] = py

class Solution(object):
    def generateSentences(self, synonyms, text):
        """
        :type synonyms: List[List[str]]
        :type text: str
        :rtype: List[str]
        """
        u = UnionFind()
        for a,b in synonyms:
            u.union(a,b)

        groups = defaultdict(list)
        for word in u.parent:
            root = u.find(word)
            groups[root].append(word)
        for key in groups:
            groups[key] = sorted(groups[key])
        #print(groups)

        words = text.split(" ")
        #print(words)
        m = len(words)
        res = []
        def backtrack(index,cur):
            if index == m:
                res.append(" ".join(cur))
                return
            
            word = words[index]
            choice = [word]
            if word in u.parent:
                choice = groups[u.find(word)]
            
            for option in choice:
                cur.append(option)
                backtrack(index+1, cur)
                cur.pop()
        backtrack(0,[])
        return res
            
            