class Player:
    
    def __init__(self, plyr_info_dict):
        
        self.plyr_info_dict = plyr_info_dict
        self.name = plyr_info_dict["name"]
        self.age = plyr_info_dict["age"]
        self.position = plyr_info_dict["position"]
        self.team = plyr_info_dict["team"]
        
        # players.append(self.plyr_dict)
        
    def display_Info(self):
        print(self.name)
        print(self.age)
        print(self.position)
        print(self.team)
        
    @classmethod
    def get_team(cls, team_list):
        
        new_team = []

        for player in range(len(team_list)):
            
            # print(team_list[player])

            plyr = cls(team_list[player])
            # plyr.display_Info()
            # print(kevin.plyr_info_dict)

            new_team.append(plyr.plyr_info_dict)
        # print(new_team)
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

def build_test_team():
    
    test_team = []
    
    for player in range(len(players)):
        
        # print(players[player])

        plyr = Player(players[player])
        # plyr.display_Info()

        test_team.append(plyr.plyr_info_dict)
    # print(test_team)
    
    return test_team
# print(build_test_team())

# Ninja Bonus: Add an @class method called
# get_team(cls, team_list) that, given a list of dictionaries populates and returns a new list of Player objects.
print(Player.get_team(build_test_team()))

