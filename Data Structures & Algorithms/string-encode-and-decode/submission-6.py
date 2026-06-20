class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for s in strs:
            encoded.append(str(len(s)))
            encoded.append('#')
            encoded.append(s)
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):
            j = i + 1
            while s[j] != '#':
                j += 1
            i = j + 1 + int(s[i:j])
            decoded.append(s[j+1:i])
        return decoded