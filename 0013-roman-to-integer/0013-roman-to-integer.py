class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        special_case = {"I": {"IV" : 4, "IX" : 9}, "X": {"XL": 40, "XC":90}, "C":{"CD": 400, "CM":900}}
        basic_case = {"I": 1, "V":5, "X":10, "L":50, "C": 100, "D":500, "M":1000}
        n = len(s)
        total = 0
        i = 0
        while i < n:
            ch = s[i]
            if ch not in special_case:
                total += basic_case[ch]
            else:
                if i + 1 < n:
                    new_str = s[i:i+2]
                    if new_str in special_case[ch]:
                        total += special_case[ch][new_str]
                        i += 1
                    else:
                        total += basic_case[ch]
                else:
                    total += basic_case[ch]
            i += 1
        return total
            