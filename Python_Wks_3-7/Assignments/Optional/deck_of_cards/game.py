from classes.deck import Deck
import random as rdm
import numpy as np
import copy

# Player Creation
dealer = {"name":"Dealer", "hand":[]}
player1 = {"name":"Player_1", "hand":[]}
player2 = {"name":"Player_2", "hand":[]}
players = [dealer,player1,player2]

# Deck Creation
deck_number = 6
one_deck = Deck().deck_array
start_over_deck = []

# Create Start Deck by Iterating through adding multiple decks
for deck in range(deck_number):
    start_over_deck += one_deck
# print(len(start_over_deck))

# Create Copy of Start Deck
combined_deck = copy.deepcopy(start_over_deck)

# Create Bucket and Iteration Variables
deck_out = []
points_dict = {}
deal_count = 0
score = {}

# Randomly Pick a Card
def deal():
    # print(deck_in)
    rand_idx = rdm.randint(0,len(combined_deck)-1)
    # print(len(combined_deck))
    # print(rand_idx)
    random_card = combined_deck[rand_idx]

    # print(random_card)
    combined_deck.pop(rand_idx)
    # print(deck_in)
    deck_out.append(random_card)
    # print(deck_out)
    
    return random_card

# deal()
# print(deck_in)
# print(deck_out)
# deal()
# print(deck_in)
# print(deck_out)
# deal()
# print(deck_in)
# print(deck_out)

# # Initial Deal To Players
def gameSetup():
    
    # Bring in the overall deal count
    global deal_count
    
    # Append a random card by calling the deal function
    for player in players:
        for card in range(2):
            player["hand"].append(deal())
    
    # Print out the hand for each player
    for x, y in zip(range(len(players)),(players)):
        print(f"{players[x]['name']}'s Hand: {y['hand']}") 
        
    # print(deck_in)
    # print(deck_out) 
    
    # Incriment the deal total
    deal_count = deal_count + 1
        
    # Create Dictionary for Player Scores
    for idx in range(len(players)):
        if f"{players[idx]['name']}" not in score.keys():
            score[f"{players[idx]['name']}"] = 0
        else:
            print("Player already in dictionary")
            
    print(f"Starting Score: {score}")
    
    return players
    
gameSetup()

# Score Hand
def scoreHand():
    
    # Point Bucket
    max_value_array = []
    
    # Get Players Point Score
    for player, idx in zip(players,range(len(players))):
        
        # Bucket for player points
        point_bucket = 0
        
        # Get card info
        for card in player["hand"]:
                
                suit = card[0]
                point_value = card[1]
                name = card[2]
                
                point_bucket += point_value
                
        # Print each players total points
        print(f"{players[idx]['name']}'s Points: {point_bucket}")
        
        # Print Highest Score Point Bucket
        max_value_array.append(point_bucket)
    
    # print(max_value_array)

    # Check Highest Score index
    max_value = max(max_value_array)
    max_value_index = max_value_array.index(max_value)
    # print(max_value_index)
    
    # Create variables for each data point in print below
    winner_card_1 = players[max_value_index]["hand"][0][2]
    winner_suit_1 = players[max_value_index]["hand"][0][0]
    winner_card_2 = players[max_value_index]["hand"][1][2]
    winner_suit_2 = players[max_value_index]["hand"][1][0]
    
    # Print out the score
    print(f"\n{players[max_value_index]['name']} is the Winner\nTotal Points: {point_bucket}\nHand: {winner_card_1} of {winner_suit_1}, {winner_card_2} of {winner_suit_2}\n")      

    # Incriment Player's Score Dictionary
    score[f"{players[max_value_index]['name']}"] += 1
        
    # Clear Players Hands
    for player in players:
        player["hand"] = []
        # print(player["hand"])
        
    print(f"Single Hand Score: {score}\n")
    print("New Game ================> \n")

def reset_Deck():
    
    # Insert global variables
    global combined_deck
    global start_over_deck
    
    # Reset Deck 
    combined_deck = start_over_deck

# Keep Game Playing until 50 cards and then reset
while len(combined_deck) > 50:
    scoreHand()
    gameSetup()
else:
    reset_Deck()
    
print(f"\nDeck Length: {len(combined_deck)}")
print(f"Number of Deals: {deal_count}")
print(f"Final Score: {score}")