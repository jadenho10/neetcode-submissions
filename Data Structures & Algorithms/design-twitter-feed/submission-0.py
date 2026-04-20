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

        # ensure self-follow
        self.followMap[userId].add(userId)

        # push the most recent tweet for each followee
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap and self.tweetMap[followeeId]:
                idx = len(self.tweetMap[followeeId]) - 1
                cnt, tw = self.tweetMap[followeeId][idx]
                heappush(minHeap, [cnt, tw, followeeId, idx - 1])

        # now merge-pop up to 10 tweets
        while minHeap and len(res) < 10:
            cnt, tw, fid, idx = heappop(minHeap)
            res.append(tw)
            if idx >= 0:
                cnt2, tw2 = self.tweetMap[fid][idx]
                heappush(minHeap, [cnt2, tw2, fid, idx - 1])

        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followMap[followerId].discard(followeeId)
