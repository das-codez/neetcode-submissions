class Twitter:

    def __init__(self):
        self.count = 0
        self.tweets = defaultdict(list)
        self.followings = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.count, tweetId])
        self.count-=1

    def getNewsFeed(self, userId: int) -> List[int]:
        ans = []
        heap = []

        self.followings[userId].add(userId)
        for fid in self.followings[userId]:
            if fid in self.tweets:
                index = len(self.tweets[fid]) - 1
                count, tweetId = self.tweets[fid][index]
                heap.append([count, tweetId, fid, index - 1])
        heapq.heapify(heap)
        while heap and len(ans) < 10:
            count, tweetId, fid, index = heapq.heappop(heap)
            ans.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweets[fid][index]
                heapq.heappush(heap, [count, tweetId, fid, index - 1])
        return ans

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followings[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followings[followerId]:
            self.followings[followerId].remove(followeeId)
        
