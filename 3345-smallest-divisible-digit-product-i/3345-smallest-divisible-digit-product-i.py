class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            val = n
            p = 1
            while val > 0:
                rem = val % 10
                p *= rem
                val //= 10
            if p % t == 0:
                return n
            n += 1
        

        