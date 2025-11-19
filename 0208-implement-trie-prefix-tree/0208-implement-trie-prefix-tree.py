class Node():
    def __init__(self, ch =  None):
        self.ch = ch
        self.children = {}
        self.is_end = False

class Trie(object):

    def __init__(self):
        self.root = Node()
        

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = Node(ch)
            cur = cur.children[ch]
        cur.is_end = True
        


    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                return False
            cur = cur.children[ch]
        return cur.is_end == True
        

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        cur = self.root
        for ch in prefix:
            if ch not in cur.children:
                return False
            cur = cur.children[ch]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)