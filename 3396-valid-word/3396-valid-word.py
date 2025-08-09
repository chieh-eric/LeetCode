class Solution(object):
    def isValid(self, word):
        """
        :type word: str
        :rtype: bool
        """
        vowel = "aeiouAEIOU"
        has_vowel = has_con = False
        if len(word) < 3:
            return False
        
        for ch in word:
            if ch.isdigit() or ch.isalpha():
                if ch.isalpha():
                    if ch in vowel:
                        has_vowel = True
                    else:
                        has_con = True
            else:
                return False
        
        return  has_vowel == has_con == True