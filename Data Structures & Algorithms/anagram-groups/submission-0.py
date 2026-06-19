class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_with_sorted = [[s, sorted(s)] for s in strs]
        strs_with_sorted.sort(key=lambda x: x[1])
        res = [[strs_with_sorted[0][0]]]
        for i in range(1, len(strs_with_sorted)):
            orig_str = strs_with_sorted[i][0]
            sorted_str = strs_with_sorted[i][1]
            if sorted_str == strs_with_sorted[i-1][1]:
                res[-1].append(orig_str)
            else:
                res.append([orig_str])
        return res