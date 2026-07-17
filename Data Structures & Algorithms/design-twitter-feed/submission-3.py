class Twitter:

    def __init__(self):
        self.follow_mp = defaultdict(set)
        self.posts = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        feed = []
        
        for followeeId in self.follow_mp[userId]:
            followee_posts = self.posts[followeeId]
            if followee_posts:
                heapq.heappush(heap, (-followee_posts[-1][0], followeeId, len(followee_posts)-1))
        self_posts = self.posts[userId]
        if self_posts and userId not in self.follow_mp[userId]:
            heapq.heappush(heap, (-self_posts[-1][0], userId, len(self_posts)-1))

        while heap and len(feed) < 10:
            _, posterId, idx = heapq.heappop(heap)
            feed.append(self.posts[posterId][idx][1])
            if idx > 0:
                idx -= 1
                heapq.heappush(heap, (-self.posts[posterId][idx][0], posterId, idx))
        
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_mp[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follow_mp[followerId].discard(followeeId)

"""
follow_mp:
1: 1

posts:
1: (0, 100)

time = 1
"""