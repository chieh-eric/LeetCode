class Solution(object):
    def splitIntoFibonacci(self, num):
        """
        :type num: str
        :rtype: List[int]
        """
        n = len(num)
        self.ans = []
        def backtrack(index, sequence):
            if index == n:
                if len(sequence) >= 3:
                    self.ans = sequence[:]
                    return True
                return False

            for i in range(index+1, n+1):
                new_num = int(num[index:i])
                if (num[index] == "0" and i - index > 1) or new_num >= 2**31:
                    return False
                
                if len(sequence) >= 2:
                    if sequence[-2] + sequence[-1] == new_num:
                        sequence.append(new_num)
                        if backtrack(i, sequence):
                            return True
                        sequence.pop()
                else:
                    sequence.append(new_num)
                    if backtrack(i, sequence):
                        return True
                    sequence.pop()
            return False
        
        backtrack(0,[])
        #print(self.ans)
        return self.ans