class Solution(object):
    def countPairs(self, deliciousness):
        """
        :type deliciousness: List[int]
        :rtype: int
        """
        count = Counter(deliciousness)
        # Sort the deliciousness
        dic = {} # Key -> element, key -> True
        # dic[1] = True 
        # 4 - 3 is in the dic? Ans: yes, dic[1], dic[3]
        # 8 - 5 is in the dic?

        # Iterate the key of count
        mod = 10**9 + 7
        def combine(n):
            if n - 2 <= 0:
                return 1
            return factorial(n) // (factorial(n-2)*factorial(2))
        
        def findPower(n):
            power = 0
            val = 2
            while val**power < n:
                power += 1
            return power
        
        def checkPower(n):
            power = 0
            val = 2
            while val**power < n:
                power += 1
            return val**power == n
        ans = 0
        for key in sorted(count):
            if checkPower(key+key) and count[key] >= 2:
                ans += combine(count[key]) % mod
            power = findPower(key)
            find = 2**power
            #print(find)
            if find-key in dic:
                ans += count[find-key] * count[key] % mod
            dic[key] = True
            #print(ans)
        return ans % mod
            
