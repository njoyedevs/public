class Player:
    
    def __init__(self, plyr_info_dict):
        
        self.name = plyr_info_dict["name"]
        self.age = plyr_info_dict["age"]
        self.position = plyr_info_dict["position"]
        self.team = plyr_info_dict["team"]
        
    def display_Info(self):
        print(self.name)
        print(self.age)
        print(self.position)
        print(self.team)
        
    # Not required for the assignment but useful
    # __repr__(self) is a python system method that 
    # tells python how to handle representing that class 
    # when, for example the object is printed to the terminal.
    # def __repr__(self):
    #     display = f"Player: {self.name}, {self.age} y/o, pos: {self.position}, team: {self.team}"
    #     return display
        
    @classmethod
    def add_players(cls, plyrs_dict):
        
        player_obj = []
        for dict in plyrs_dict:
            player_obj.append(cls(dict))
            
        return player_obj
    
    @classmethod
    def get_team(cls, team_list):
        
        new_team = []

        for player in range(len(team_list)):
            
            # print(team_list[player])

            plyr = cls(team_list[player])
            
            new_team.append(plyr)

        return new_team
        
players = [
    {
        "name": "Kevin Durant", 
        "age":34, 
        "position": "small forward", 
        "team": "Brooklyn Nets"
    },
    {
        "name": "Jason Tatum", 
        "age":24, 
        "position": "small forward", 
        "team": "Boston Celtics"
    },
    {
        "name": "Kyrie Irving", 
        "age":32,
        "position": "Point Guard", 
        "team": "Brooklyn Nets"
    },
    {
        "name": "Damian Lillard", 
        "age":33,
        "position": "Point Guard", 
        "team": "Portland Trailblazers"
    },
    {
        "name": "Joel Embiid", 
        "age":32,
        "position": "Power Foward", 
        "team": "Philidelphia 76ers"
    },
    {
        "name": "DeMar DeRozan",
        "age": 32,
        "position": "Shooting Guard",
        "team": "Chicago Bulls"
    },
    {
        "name": "Nick Joye", 
        "age":39,
        "position": "Point Guard", 
        "team": "Phoenix Suns"
    }
]

test_team = Player.add_players(players)
print(test_team)

# Ninja Bonus: Add an @class method called
# get_team(cls, team_list) that, given a list of dictionaries populates and returns a new list of Player objects.
print(Player.get_team(players))