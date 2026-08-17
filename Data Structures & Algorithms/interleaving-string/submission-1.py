class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        s1_length = len(s1)
        s2_length = len(s2)

        if s1_length + s2_length != len(s3):
            return False
        
        dp = set([(0, 0)])

        for char in s3:
            new_dp = set()
            for i, j in dp:
                if i < s1_length and char == s1[i]:
                    new_dp.add((i+1, j))
                if j < s2_length and char == s2[j]:
                    new_dp.add((i, j+1))

            if len(new_dp) == 0:
                return False
            dp = new_dp

        return True
            
        