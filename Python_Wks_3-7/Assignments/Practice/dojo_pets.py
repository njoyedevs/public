class Pet:
    
# implement __init__( name , type , tricks , noise ):
    def __init__(self, name , type , tricks, noise):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 100
        self.energy = 50
        self.noise = noise
        
    # implement the following methods:
    # sleep() - increases the pets energy by 25
    def sleep(self):
        self.energy += 25
        
    # eat() - increases the pet's energy by 5 & health by 10
    def eat(self):
        self.energy += 5
        self.health += 10
        
    # play() - increases the pet's health by 5
    def play(self):
        self.health += 5
        
    # noise() - prints out the pet's sound
    def get_noise(self):
        print(self.noise)
        
    # exercise() - decreases the pet's energy by 10 and health by 5
    def exercise(self):
        self.energy -= 10
        self.health -= 5    
        
    # injury() - decreases the pet's energy by 15 and health by 30
    def injury(self):
        self.energy -= 15
        self.health -= 30  

class Ninja:
    
    # implement __init__( first_name , last_name , treats , pet_food , pet )
    def __init__(self,first_name , last_name , treats , pet_food , pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet
	
        # implement the following methods:
    # walk() - walks the ninja's pet invoking the pet play() method
    def walk(self):
        self.pet.play()
        return self
        
    # feed() - feeds the ninja's pet invoking the pet eat() method
    def feed(self):
        
        if len(self.pet_food) > 0:
            food = self.pet_food.pop()
            print(f"Feeding {self.pet.name} {food}")
            self.pet.eat()
        else:
            print("Oh no!!! you need more pet food!")
        return self
        
    # bathe() - cleans the ninja's pet invoking the pet noise() method
    def bath(self):
        self.pet.noise()
        return self
        
    #fitness() - cleans the ninja's pet invoking the pet exercise() method
    def fitness(self):
        self.pet.exercise()
        return self
        
    #accident() - cleans the ninja's pet invoking the pet injury() method
    def accident(self):
        self.pet.injury()
        return self
    
    

my_treats = ['Snausage','Bacon',"Trash Bag"]
my_pet_food = ['Pizza','Burger']

nibbles = Pet("Mr. Nibbles","Horse",['nibbles on things','is invisible'],"Hey Hey")

adrien = Ninja("Adrien","Dion",my_treats,my_pet_food, nibbles)

adrien.feed()
adrien.feed()
adrien.feed()