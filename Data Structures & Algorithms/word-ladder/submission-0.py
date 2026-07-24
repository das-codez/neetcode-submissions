class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        graph = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                graph[word[:i] + '_' + word[i+1:]].append(word)
        q = deque([(beginWord, 1)])
        seen = set()
        while q:
            word, k = q.popleft()
            if word == endWord:
                return k
            if word not in seen:
                seen.add(word)
                for i in range(len(word)):
                    neighbors = word[:i] + '_' + word[i+1:]
                    for nei in graph[neighbors]:
                        q.append((nei, k+1))
        return 0