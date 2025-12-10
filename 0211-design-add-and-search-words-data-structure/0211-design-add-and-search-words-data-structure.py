class TrieNode():
    def __init__(self):
        self.children = {}
        self.is_end = False
    
    def add(self, word):
        node = self
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True
    
    def find(self, word):
        node = self
      
        def dfs(word, index, node):
            if index == len(word):
                return node.is_end
            

            if word[index] != ".":
                if word[index] not in node.children:
                    return False
                return dfs(word, index + 1, node.children[word[index]])
            else:
                result = False
                for child in node.children.values():
                    result = result or dfs(word, index+1, child)
                return result
        return dfs(word, 0, node)

class WordDictionary(object):

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        self.root.add(word)

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return self.root.find(word)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)