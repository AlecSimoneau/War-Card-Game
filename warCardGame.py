import numpy as np
from numpy import random 
#variables
wars = 0
hands = 0 
playerAWins = 0
playerBWins = 0 
gameWon = False
winner = ""
deck = np.array([2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 11, 11, 11, 11, 12, 12, 12, 12, 13, 13, 13, 13, 14, 14, 14, 14])
#random seed to fix randomly generated numbers
np.random.seed(9)

random.shuffle(deck)

playerA_Deck = deck[:26]
playerB_Deck = deck[26:]


 
def compare(playerA_Deck,playerB_Deck,playerAWins,playerBWins,pile,gameWon,hands,winner,wars):
    
    hands += 1
        
    if (len(playerA_Deck) == 0) or (len(playerB_Deck) == 0):
        gameWon = True
        if len(playerA_Deck) == 0:
            winner = "Player B"
        else:
            winner = "Player A"
        return playerA_Deck, playerB_Deck, playerAWins, playerBWins, gameWon, hands, winner,wars
    
    if int(playerA_Deck[0]) > int(playerB_Deck[0]):
        
        # Increases Player A's wins by 1
        
        playerAWins += 1
        #print(playerAWins,playerBWins)
        # Adds the card Player B put down to the bottom of 
        # Player A's deck
        
        playerA_Deck = np.append(playerA_Deck,playerB_Deck[0])
        
        # If compare was called after a war then add the pile from the war to 
        # the bottom of Player's deck
        
        playerA_Deck = np.append(playerA_Deck,pile)
        
        # Deletes the card Player B put down from their deck
        
        mask = np.ones(len(playerB_Deck), dtype=bool)
        mask[[0]] = False
        playerB_Deck = playerB_Deck[mask,...]
        
       
    elif int(playerA_Deck[0]) < int(playerB_Deck[0]):
        
        # Increases Player B's wins by 1
        
        playerBWins += 1
        
        # Adds the card Player A put down to the bottom of 
        # Player B's deck
        
        playerB_Deck = np.append(playerB_Deck,playerA_Deck[0])
        
        # If compare was called after a war then add the pile from the war to 
        # the bottom of Player's deck
        
        playerB_Deck = np.append(playerB_Deck,pile)
        
        # Deletes the card Player A put down from their deck
        
        mask = np.ones(len(playerA_Deck), dtype=bool)
        mask[[0]] = False
        playerA_Deck = playerA_Deck[mask,...]
       
    else:
        # If neither is greater then they must be the same therefore call war
        playerA_Deck,playerB_Deck,wars,hands = war(playerA_Deck,playerB_Deck,wars,hands)
        
    # Shuffle each players hand to prevent endless loops
    # Potentially shuffle after a certain amount of hands
    random.shuffle(playerA_Deck)
    random.shuffle(playerB_Deck)
    
    return playerA_Deck, playerB_Deck, playerAWins, playerBWins, gameWon, hands, winner, wars
    
    
    
def war(playerA_Deck,playerB_Deck,wars,hands):
    
    #print("WARRR")
    wars += 1
    #because wars calls compare, this would incorrectly inflate the hands count
    hands -= 1
    
    
    if len(playerA_Deck) > 4 and len(playerB_Deck) > 4:
        
        pile = []
    
        ## Adds the top three cards in the players deck to the pile
    
        pile = np.append(pile,playerA_Deck[0:4])
        pile = np.append(pile,playerB_Deck[0:4])

        ## This deletes the first three elements in the Player A and B decks
        ## I don't know why it works but it was the only solution I could find
    
            #Deletes for Player A
        mask = np.ones(len(playerA_Deck), dtype=bool)
        mask[[0,1,2,3]] = False
        playerA_Deck = playerA_Deck[mask,...]    

            #Deletes for Player B
        mask = np.ones(len(playerB_Deck), dtype=bool)
        mask[[0,1,2,3]] = False
        playerB_Deck = playerB_Deck[mask,...]    
    
        #print(pile,playerA_Deck,playerB_Deck)
    
        oldPlayerAWins = playerAWins
        # Calls Compare to see who wins the war
        
        compare(playerA_Deck, playerB_Deck,playerAWins,playerBWins,pile,gameWon,hands,winner,wars)
        
        if playerAWins > oldPlayerAWins:
            playerA_Deck = np.append(playerA_Deck,pile)
        else:
            playerB_Deck = np.append(playerB_Deck,pile)
            
        #This elif and the else are for if either player has less than 4 cards 
        #which would break the code above
        
    elif len(playerA_Deck) <= 4:
        
        #checks how many cards are left in Player A's deck
        cardsLeft = len(playerA_Deck)
        pile = []

        ## Adds the top three cards in the players deck to the pile

        pile = np.append(pile,playerA_Deck[0:cardsLeft-1])
        pile = np.append(pile,playerB_Deck[0:4])

        ## This deletes the first three elements in the Player A and B decks
        ## I don't know why it works but it was the only solution I could find

        #Deletes for Player A
        mask = np.ones(len(playerA_Deck), dtype=bool)
        
        #for loop to make the delete work
        for i in range(0,cardsLeft-1):
            mask[[i]] = False
        playerA_Deck = playerA_Deck[mask,...]    

        #Deletes for Player B
        mask = np.ones(len(playerB_Deck), dtype=bool)
        mask[[0,1,2,3]] = False
        playerB_Deck = playerB_Deck[mask,...]    

        oldPlayerAWins = playerAWins
        # Calls Compare to see who wins the war
        
        compare(playerA_Deck, playerB_Deck,playerAWins,playerBWins,pile,gameWon,hands,winner,wars)
        
        if playerAWins > oldPlayerAWins:
            playerA_Deck = np.append(playerA_Deck,pile)
        else:
            playerB_Deck = np.append(playerB_Deck,pile)        
        
    else:
        
        #checks how many cards are left in Player B's deck
        cardsLeft = len(playerB_Deck)
        pile = []

        ## Adds the top three cards in the players deck to the pile

        pile = np.append(pile,playerB_Deck[0:cardsLeft-1])
        pile = np.append(pile,playerA_Deck[0:4])

        ## This deletes the first three elements in the Player A and B decks
        ## I don't know why it works but it was the only solution I could find

        #Deletes for Player B
        mask = np.ones(len(playerB_Deck), dtype=bool)
        
        #for loop to make the delete work
        for i in range(0,cardsLeft-1):
            mask[[i]] = False
        playerB_Deck = playerB_Deck[mask,...]    

        #Deletes for Player A
        mask = np.ones(len(playerA_Deck), dtype=bool)
        mask[[0,1,2,3]] = False
        playerA_Deck = playerA_Deck[mask,...]    

        
        oldPlayerAWins = playerAWins
        # Calls Compare to see who wins the war
        
        compare(playerA_Deck, playerB_Deck,playerAWins,playerBWins,pile,gameWon,hands,winner,wars)
        
        if playerAWins > oldPlayerAWins:
            playerA_Deck = np.append(playerA_Deck,pile)
        else:
            playerB_Deck = np.append(playerB_Deck,pile)               
        
    return playerA_Deck,playerB_Deck,wars,hands 

while (gameWon == False):
    playerA_Deck, playerB_Deck, playerAWins, playerBWins, gameWon, hands, winner, wars = compare(playerA_Deck, playerB_Deck, playerAWins, playerBWins, [], gameWon, hands, winner, wars)
# if hands == 100000:
#     print("Game exited after 100000 hands")
# else:    
print(playerA_Deck,playerB_Deck)
print(str(winner) + " won the game after " + str(hands) + " hands")
print("There were " + str(wars) + " wars \nPlayer A won " + str(playerAWins) + " hands")
print("Player B won " + str(playerBWins) + " hands")
    
## Generated the numbers for the deck
# for i in range(2,15):
#     for j in range(0,4):
#         deck.append(i)
# print(deck)
