class TrieNode():
    def __init__(self, ch):
        self.ch = ch
        self.children = {}
        self.is_end = False
    
    def add(self, word):
        node = self
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode(ch)
            node = node.children[ch]
        node.is_end = True
    
class MagicDictionary(object):

    def __init__(self):
        self.root = TrieNode("#")

    def buildDict(self, dictionary):
        """
        :type dictionary: List[str]
        :rtype: None
        """
        node = self.root
        for word in dictionary:
            node.add(word)

    def search(self, searchWord):
        """
        :type searchWord: str
        :rtype: bool
        """
        
        def dfs(node, word, index, modification):
            if modification < 0:
                return False
            
            if index == len(word):
                return not modification and node.is_end
            
            for nei in node.children.values():
                if nei.ch == word[index]:
                    if dfs(nei, word, index + 1, modification):
                        return True
                else:
                    if dfs(nei, word, index + 1, modification - 1):
                        return True
            return False
        return dfs(self.root, searchWord, 0, 1)

# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)