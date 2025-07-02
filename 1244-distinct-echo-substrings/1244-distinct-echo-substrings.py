class Solution(object):
    def distinctEchoSubstrings(self, text):
        """
        :type text: str
        :rtype: int
        """
        some_strings = set()
        for j in range(len(text)):
            for i in range(j):
                if text.startswith(text[i:j], j):
                    some_strings.add(text[i:j])
        return len(some_strings)