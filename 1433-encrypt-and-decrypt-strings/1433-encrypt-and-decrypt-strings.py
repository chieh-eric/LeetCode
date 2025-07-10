from collections import defaultdict
class Encrypter(object):

    def __init__(self, keys, values, dictionary):
        """
        :type keys: List[str]
        :type values: List[str]
        :type dictionary: List[str]
        """
        self.encry = defaultdict(list)
        self.decry = defaultdict(list)
        n = len(keys)
        for i in range(n):
            self.encry[keys[i]].append(values[i])
            self.decry[values[i]].append(keys[i])
        self.cipher = defaultdict(int)
        for word in dictionary:
            c = []
            n = len(word)
            ch = ""
            for i in range(n):
                ch += word[i]
                if ch in self.encry:
                    c.append(self.encry[ch][0])
                    ch = ""
            if ch:
                break
            self.cipher["".join(c)] += 1

    def encrypt(self, word1):
        """
        :type word1: str
        :rtype: str
        """
        output = []
        for ch in word1:
            output.append(self.encry[ch][0])
        return "".join(output)
        

    def decrypt(self, word2):
        """
        :type word2: str
        :rtype: int
        """
        return self.cipher[word2]
        


        


# Your Encrypter object will be instantiated and called as such:
# obj = Encrypter(keys, values, dictionary)
# param_1 = obj.encrypt(word1)
# param_2 = obj.decrypt(word2)