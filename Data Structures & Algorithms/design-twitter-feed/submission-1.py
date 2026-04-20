from heapq import heappush, heappop, heapify
class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list) # userID: [count, tweetID]
        self.followMap = defaultdict(set) # userID: followerID

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1

    #tweet IDs
    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []

        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]:
            # want to get last tweet posted by followee 
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1 
                count, tweet = self.tweetMap[followeeId][index]
                heappush(minHeap, [count, tweet, followeeId, index - 1])

        while minHeap and len(res) < 10:
            count, tweet, followeeId, index = heappop(minHeap)
            res.append(tweet)
            if index >= 0:
                count, tweet = self.tweetMap[followeeId][index]
                heappush(minHeap, [count, tweet, followeeId, index - 1])

        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followMap[followerId].discard(followeeId)
