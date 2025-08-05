class TrieNode():
    def __init__(self):
        self.children = {}
        self.count = 0
    
    def add(self,word):
        node = self
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
            node.count += 1
    
    def find(self,word):
        node = self
        c = 0
        
        for ch in word:
            node = node.children[ch]
            c += node.count
            
        return c

class Solution(object):
    def sumPrefixScores(self, words):
        """
        :type words: List[str]
        :rtype: List[int]
        """
        root = TrieNode()
        for word in words:
            root.add(word)
        res = []
        for word in words:
            res.append(root.find(word))
        return res