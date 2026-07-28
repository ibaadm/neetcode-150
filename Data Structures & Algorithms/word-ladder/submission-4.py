class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        n = len(wordList[0])
        wordPatterns = defaultdict(list)
        for word in wordList:
            chars = list(word)
            for i in range(n):
                tmp = chars[i]
                chars[i] = '*'
                wordPatterns["".join(chars)].append(word)
                chars[i] = tmp
        
        q = deque([beginWord])
        visited = {beginWord}
        dist = 1
        while q:
            for _ in range(len(q)):
                word = q.popleft()
                chars = list(word)
                for i in range(n):
                    tmp = chars[i]
                    chars[i] = '*'
                    for next_word in wordPatterns["".join(chars)]:
                        if next_word in visited:
                            continue
                        if next_word == endWord:
                            return dist+1
                        visited.add(next_word)
                        q.append(next_word)
                    chars[i] = tmp
            dist += 1
             
        return 0