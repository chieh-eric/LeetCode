class Solution(object):
    def decodeMessage(self, key, message):
        """
        :type key: str
        :type message: str
        :rtype: str
        """
        mapper = {}
        shift = 0

        for ch in key:
            if ch != " " and ch not in mapper:
                mapper[ch] = chr(ord('a')+shift)
                shift += 1
        res = ""
        mapper[" "] = " "
        #print(mapper)
        for ch in message:
            res += mapper[ch]
        return res
