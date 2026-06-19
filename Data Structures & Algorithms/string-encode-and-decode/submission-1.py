class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for s in strs:
            for c in s:
                if c == '\\':
                    encoded.append('\\')
                    encoded.append('\\')
                else:
                    encoded.append(c)
            encoded.append('\\')
            encoded.append('z')
        return ''.join(encoded)
                    

    def decode(self, s: str) -> List[str]:
        decoded = []
        curr = []
        backslash = False
        for c in s:
            if backslash:
                if c == '\\':
                    curr.append('\\')
                else:
                    decoded.append(''.join(curr))
                    curr = []
                backslash = False
            elif c == '\\':
                backslash = True
            else:
                curr.append(c)
        return decoded
