class TrieNode():
    def __init__(self):
        self.children = {}
        self.is_end = False
    
    def add(self,s):
            node = self
            for ch in s:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.is_end = True

    def search(self, s, index, mismatch_count):
            cur = self
            for char, node in cur.children.items():
                is_diff = char != s[index]
                if mismatch_count + is_diff <= 1 and node.search(s,index+1,mismatch_count+is_diff):
                    return True
            
            return self.is_end and mismatch_count == 1


class Solution(object):
    def differByOne(self, dicti):
        """
        :type dict: List[str]
        :rtype: bool
        """
        root = TrieNode()

        for word in dicti:
            root.add(word)
            if root.search(word,0,0):
                return True
        return False

                    
    
    
