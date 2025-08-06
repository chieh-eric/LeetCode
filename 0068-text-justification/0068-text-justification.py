class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        groups = []
        word_lengths = []
        index = 0
        n = len(words)
        cur_lenght = 0
        while index < n:
            temp = []
            cur_length = 0
            word_length = 0
            while index < n and cur_length - 1 <= maxWidth:
                word_length += len(words[index])
                temp.append(words[index])
                cur_length += len(words[index]) + 1
                index += 1
                
            
            if cur_length - 1 > maxWidth:
                index -= 1
                word_length -= len(words[index])
                temp.pop()
            groups.append(temp)
            word_lengths.append(word_length)

       # print(groups)
        #print(word_lengths)
        res = []
        for i, group in enumerate(groups):
            temp = ""
            spaces = maxWidth - word_lengths[i]
            slots = len(group) - 1
            if i == len(groups) - 1:
                for j, word in enumerate(group):
                    if j == len(group) - 1:
                        
                        temp += word
                        m = len(temp)
                        temp += " "*(maxWidth-m)
                    else:
                        temp += word + " "
            else:
                for word in group:
                    slot = (spaces+slots-1) // slots if slots != 0 else spaces
                    temp += word + slot*" "
                    slots -= 1
                    spaces -= slot
            res.append(temp)
        return res
                