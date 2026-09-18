class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n not in seen:
            seen.add(n)
            if n == 1:
                return True
            new = 0
            while n:
                n, d = divmod(n, 10)
                new += d ** 2
            n = new
        return False