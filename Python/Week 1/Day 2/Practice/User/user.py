class User:
    def __init__(self,first_name,last_name,email,age,rewards):

        self.FirstName = first_name
        self.LastName = last_name
        self.Email = email
        self.Age = age
        self.is_rewards_member = rewards     #default values.
        self.gold_card_points = 0           #default values.

        # if self.is_rewards_member == False:
        #             self.is_rewards_member = True
        

    def display_info(self):
        print (f"\n First name : {self.FirstName} \n Last Name : {self.LastName} \n Email : {self.Email} \n Age : {self.Age} \n Rewards : {self.is_rewards_member} \n Gold card points : {self.gold_card_points} \n **********************************")

    def spend_points(self,amount):
        self.Amount = amount
        print (f" \n Amount spent by {self.FirstName} : {self.Amount} \n **********************************")





    def membership_tester(self):  #Membership tester and enroller
            if self.is_rewards_member == False:
                            self.is_rewards_member = True
            self.gold_card_points = 200
            self.gold_card_points = self.gold_card_points - self.Amount

                    


User1 = User("John","Coding","CodingJohn@mail.com",72,False)

User1.spend_points(50)
User1.membership_tester()

User1.display_info()



User2 = User("John jr","Dojo","DojoJohnJr@mail.com",27,True)

User2.spend_points(80)
User2.membership_tester()

User2.display_info()


