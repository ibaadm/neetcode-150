class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if x == 0:
            return 0
        
        neg = False
        if n < 0:
            neg = True
            n = -n
        
        bit_indices = []
        i = 0
        while n:
            if n & 1:
                bit_indices.append(i)
            n >>= 1
            i += 1

        res = 1
        p = 0
        i = 0
        while True:
            if p == bit_indices[i]:
                res *= x
                i += 1
                if i == len(bit_indices):
                    break
            x *= x
            p += 1
        
        if neg:
            res = 1 / res
        return res
