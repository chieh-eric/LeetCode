from collections import defaultdict
class Solution(object):
    def decodeCiphertext(self, encodedText, rows):
        """
        :type encodedText: str
        :type rows: int
        :rtype: str
        """
        # Approach
        # Know the length and width of the matrix
        # Place the character in this matrix
        # Start the blue line direciton traversal

        # Use dictionary, key -> group of the text, value -> character of the text
        if not encodedText:
            return ""
        m = rows
        n = len(encodedText) // m
        matrix = [[""]*n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                matrix[i][j] = encodedText[i*n+j]
        #print(matrix)
        original = []
        dic = defaultdict(str)
        for i in range(m):
            for j in range(n):
                dic[i-j] += matrix[i][j]
        #print(dic)
        for key in sorted(dic, reverse = True):
            if key > 0 :
                continue
            original.append(dic[key])
        original = "".join(original)
        end = len(original) - 1
        while original[end] == " ":
            end -= 1
        return original[:end+1]

        