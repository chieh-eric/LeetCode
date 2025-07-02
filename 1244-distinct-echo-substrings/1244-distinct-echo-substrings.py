class Solution(object):
    def distinctEchoSubstrings(self, text):
        """
        :type text: str
        :rtype: int
        """
        valid = set()
        for j in range(len(text)):
            for i in range(j):
                if text.startswith(text[i:j],j):
                    valid.add(text[i:j])
        return len(valid)