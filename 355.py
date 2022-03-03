# Design Twitter
class User:
     def __init__(self,userId):
            self.userId = userId
            self.following = set()
            self.following.add(userId)

class Twitter:

    def __init__(self):
        self.usersDict = {}
        self.tweets = []

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId in self.usersDict: user =  self.usersDict[userId]
        else: 
            user = User(userId)
            self.usersDict[userId] = user
        self.tweets.append((userId,tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId in self.usersDict: user =  self.usersDict[userId]
        else: return []
        last_10_tweets = []

        i = 0
        while len(last_10_tweets) < 10:
            if i == len(self.tweets): break
            elif self.tweets[-1-i][0] in user.following:
                last_10_tweets.append(self.tweets[-1-i][1])
            i += 1
        return last_10_tweets
    
    def follow(self, followerId: int, followeeId: int) -> None:  
        if followerId in  self.usersDict: follower =  self.usersDict[followerId]
        else: 
            follower = User(followerId)
            self.usersDict[followerId] = follower
        follower.following.add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:     
        if followerId in self.usersDict: follower =  self.usersDict[followerId]
        else: return []
        if followeeId in  follower.following: follower.following.remove(followeeId)