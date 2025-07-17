import bisect
class Solution(object):
    def atMostNGivenDigitSet(self, digits, n):
        """
        :type digits: List[str]
        :type n: int
        :rtype: int
        """
        s = str(n)
        length = len(s)
        m = len(digits)
        count = 0
        for i in range(1,length):
            count += m**i
        
       # print(count)
        while length > 0:
            handle = s[-length]
            idx = bisect.bisect_left(digits,handle)
            valid = idx if idx > 0 else 0
            count += valid*((m)**(length-1))
            print(count)
            
            if idx >= m or digits[idx] != handle:
                break
           
            if length == 1 and digits[idx] == handle:
                #print("inside")
                count += 1
            length -= 1
            
        #print(count)
        return count