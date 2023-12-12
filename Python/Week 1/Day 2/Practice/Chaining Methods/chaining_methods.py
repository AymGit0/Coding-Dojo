class User:

    def __init__(self,first_name,last_name,email,age):
        self.first_name=first_name
        self.last_name=last_name
        self.email=email
        self.age=age
        self.is_rewards_member=False
        self.gold_card_points=0

    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(self.is_rewards_member)
        print(self.gold_card_points)
        return self

    def enroll(self):
        if self.is_rewards_member==False:
            self.gold_card_points=200
            self.is_rewards_member=True
        else:
            print("User already a member.")
            self.is_rewards_member=False
        return self


    def spend_points(self,amount):
        if self.gold_card_points>= amount:
            self.gold_card_points-=amount
        else:
            print(f"User {self.first_name} doesn't have enough points.")
        return self

user1=User("Joe","Mark","JoeMark@gmail.com",27)

user1.display_info().enroll()


user2=User("Mark","Joe","NarkJoe@gmail.com",2)

user3=User("John","Dean","JohnDean@gmail.com",72)

user1.spend_points(50)
user2.enroll().spend_points(80)


user1.display_info()
user2.display_info()
user3.display_info().spend_points(40)
