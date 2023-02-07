class User:
    
    def __init__(self, first_name, last_name, email, age, gold_card_points=0):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = gold_card_points
        
    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(self.is_rewards_member)
        print(self.gold_card_points)
        return self
        
    def enroll(self):
        self.is_rewards_member = True
        self.gold_card_points = 200
        return self
        
    def spend_points(self,amount):
        if self.gold_card_points >= amount:
            self.gold_card_points -= amount
        else:
            print("Insufficient Points")
        return self
    
    def is_member(self):
        if self.is_rewards_member == True:
            print("User already a member")
            return False
        else:
            print("User not a member")
            return True
    
user_1 = User("John","Doe","john.doe@gmail.com",30)
user_1.display_info().enroll().display_info().spend_points(50).display_info()
user_1.is_member()


user_2 = User("Jane","Doe","jane.doe@gmail.com",30)
user_2.display_info().enroll().spend_points(80).display_info()
user_2.is_member()

user_3 = User("James","Jones","james.jones@gmail.com",20, gold_card_points=20)
user_3.display_info().spend_points(40).display_info()
user_3.is_member()