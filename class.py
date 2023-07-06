class User:
    def __init__(self,user_id,user_name) :
        self.id=user_id
        self.name=user_name
        self.followers=0
        self.following=0
        print(user_id,user_name)
    def follow(self,followers):
        u1.followers+=1
        self.following+=1
u1=User(10,"Sudha")
u2=User(20,"Smith")  
u1.follow(u2)

