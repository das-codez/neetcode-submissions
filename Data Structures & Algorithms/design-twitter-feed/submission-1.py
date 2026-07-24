class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list)
        self.followMap = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -=1

    def getNewsFeed(self, userId: int) -> List[int]:
        ans = []
        heap = []
        self.followMap[userId].add(userId)
        #first loop adds all the last tweets of the followers + user
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1
                count, tweetId = self.tweetMap[followeeId][index]
                heap.append([count, tweetId, followeeId, index - 1])
        heapq.heapify(heap)
        #builds answer by going through the tweet list
        while heap and len(ans) < 10:
            count, tweetId, followeeId, index = heapq.heappop(heap)
            ans.append(tweetId)
            #adds next tweet of curr tweeter to heap if there are more tweets
            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(heap, [count, tweetId, followeeId, index - 1])
        return ans

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
