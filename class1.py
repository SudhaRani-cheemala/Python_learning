class User:
    def __init__(self,user_id,user_name):
        self.id=user_id
        self.name=user_name
        self.followers=0
        self.following=0
    def follow(self,user):  
        user.followers+=1
        self.following+=1  
user1=User("001","Sudha")      
print(user1.id) 
user2=User("002","Rani")
print(user2.id)
user1.follow(user2)
print(user1.followers)
print(user1.following)
# ---------------methods in class--------------------------------
