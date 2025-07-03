
class intern:

    def __init__(self,id,name,exp):
        self.id=id
        self.name=name
        self.exp=exp
        self.connected=0
        self.followed=0
        self.following=0

    def connect(self,intern):
        self.connected+=1
        intern.connected+=1
    def follow(self,user):
        self.following+=1
        user.followed+=1

user1=intern(10,"shrav",0)
user2=intern(21,"vaish",0)

user1.connect(user2)
user1.follow(user2)

print(user1.connected)
print(user2.connected)
print(user1.following)
print(user1.followed)
print(user2.following)
print(user2.followed)

