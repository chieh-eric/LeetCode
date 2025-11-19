class Node():
    def __init__(self, ch = None):
        self.ch = ch
        self.children = {}
        self.is_end = False

class Solution(object):
    def replaceWords(self, dictionary, sentence):
        """
        :type dictionary: List[str]
        :type sentence: str
        :rtype: str
        """
        root = Node()

        for word in dictionary:
            cur = root
            for ch in word:
                if ch not in cur.children:
                    cur.children[ch] = Node(ch)
                cur = cur.children[ch]
            cur.is_end = True
        
        ans = []
        words = sentence.split(" ")
        #print(words)
        for word in words:
            cur = root
            cur_str = ""
            found = False
            for ch in word:
                if ch in cur.children:
                    cur_str += ch
                    cur = cur.children[ch]
                    if cur.is_end:
                        found = True
                        ans.append(cur_str)
                        break
                else:
                    break
            if not found:
                ans.append(word)
        #print(ans)
        return " ".join(ans)

