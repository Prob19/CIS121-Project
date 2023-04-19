import random
class BasketballPlayer:
    def __init__(self, name, team_name):
        self.name = name #created player name
        self.team_name = team_name 
        self.score = 0 #sets player score as 0
    def Player_play_game(self):#score for each individual player, not total points for the team
        self.score = random.randint(0, 50)#picks a random number between 0 and 50 and set that as the player score
class BasketballGame:
    def __init__(self, my_team, opponent_team, team_name):
        self.team_name = team_name
        self.my_team = my_team
        self.opponent_team = opponent_team
    def create_team(self):
        self.my_team = [] #empty list to hold teams players
        self.team_name = str(input("Enter a Team Name: "))#users created team name
        for i in range(3): #Appends 3 players to the created team
            player_name = input(f"Enter player {i} name: ")
            self.my_team.append(BasketballPlayer(player_name))
    def Team_play_game(self):
        print(f"{self.team_name} vs {self.opponent_team}")
        for player in self.my_team:
            player.Player_play_game() #calls player play game method to get a random number to set as each players points scored
            opponent_player = random.choice(self.opponent_team)#picks random player from the oppenent team 
            opponent_score = random.randint(0, 50) #sets random number from 0-50 and uses the randomly picked opponent player and assigns them the random number as their points scored
            print(f"{player.name} scored {player.score} points on {opponent_player} and {self.opponent_team} scored {opponent_score} points")
        my_team_score = sum([player.score for player in self.my_team])  # calculate total score for my team
        opponent_team_score = random.randint(50, 150)#sets oppenent teams score with a number between 50 and 150
        print(f"Game result: My Team {my_team_score} - {opponent_team_score} {self.opponent_team}")
        if my_team_score > opponent_team_score:
            print("My Team wins!")
        else:
            print(self.opponent_team, "wins")
#Hard coded teams with players
opponent_teams = {
    "Timberwolves": ["Karl Anthony-Towns", "Rudy Gobert", "Anthony Edwards"],
    "Nets": ["Nic Claxton", "Cam Thomas", "Seth Curry"],
    "Clippers": ["Paul George", "Kawhi Leonard", "Marcus Morris"],
    "Magic": ["Jalen Suggs", "Franz Wagner", "Cole Anthony"],
    "Kings": ["Damontis Sabonis", "Kevin Huerter", "DeAaron Fox"],
    "Heat": ["Jimmy Butler", "Tyler Herro", "Bam Adebayo"]
}
#User creates team
my_team = []
for i in range(3): #
    player_name = input(f"Enter player {i+1} name: ")
    my_team.append(BasketballPlayer(player_name, "My Team"))
# Prompt the user to choose an opponent team
print("\nChoose an opponent team:")
for team_name in opponent_teams.keys():
    print(team_name)
choice = input("Enter team name: ")
opponent_team = opponent_teams[choice]
#object called to play game
game = BasketballGame(my_team, opponent_team)
game.Team_play_game()








