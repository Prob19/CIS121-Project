
import random
class BasketballPlayer:
    def __init__(self, name, team_name):
        self.name = name
        self.team_name = team_name
        self.score = 0  # initialize player's score to 0
    def play_game(self):
        self.score = random.randint(0, 50)  # simulate player's score using a random integer between 0 and 50
class BasketballGame:
    def __init__(self, my_team, opponent_team, team_name):
        self.team_name = team_name
        self.my_team = my_team
        self.opponent_team = opponent_team
    def create_team(self):
        self.my_team = []
        self.team_name = str(input("Enter a Team Name: "))
        for i in range(3):
            player_name = input("Enter player",i, "name: ")
            self.my_team.append(BasketballPlayer(player_name))
    def play_game(self):
        print(self.team_name , " V.S " ,self.opponent_team)
        for player in self.my_team:
            player.play_game()  # simulate player's score
            opponent_player = random.choice(self.opponent_team)
            opponent_score = random.randint(0, 50)  # simulate opponent player's score
            print(player.name, "scored" ,player.score, "points on", opponent_player, "and", self.opponent_team, "scored" ,opponent_score, "points")
        my_team_score = sum([player.score for player in self.my_team])  # calculate total score for my team
        opponent_team_score = random.randint(0, 150)  # simulate opponent team's score
        print(f"Game result: My Team {my_team_score} - {opponent_team_score} {self.opponent_team}")
        if my_team_score > opponent_team_score:
            print("My Team wins!")
        else:
            print(f"{self.opponent_team} wins!")
# Pre-defined opponent teams
opponent_teams = {
    "Timberwolves": ["Karl Anthony-Towns", "Rudy Gobert", "Anthony Edwards"],
    "Nets": ["Nic Claxton", "Cam Thomas", "Seth Curry"],
    "Clippers": ["Paul George", "Kawhi Leonard", "Marcus Morris"],
    "Magic": ["Jalen Suggs", "Franz Wagner", "Cole Anthony"],
    "Kings": ["Damontis Sabonis", "Kevin Huerter", "DeAaron Fox"],
    "Heat": ["Jimmy Butler", "Tyler Herro", "Bam Adebayo"]
}
# Prompt the user to create their team
my_team = []
for i in range(3):
    player_name = input(f"Enter player {i+1} name: ")
    my_team.append(BasketballPlayer(player_name, "My Team"))
# Prompt the user to choose an opponent team
print("\nChoose an opponent team:")
for team_name in opponent_teams.keys():
    print(f"{team_name}")
choice = input("Enter team name: ")
opponent_team = opponent_teams[choice]
# Play the game
game = BasketballGame(my_team, opponent_team)
game.play_game()
