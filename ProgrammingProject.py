import random
"""
Timberwolves=["Karl Anthony-Towns","Rudy Gobert","Anthony Edwards"]
Nets=["Nic Claxton","Cam Thomas","Seth Curry"]
Clippers=["Paul George","Kawhi Leonard","Marcus Morris"]
Magic=["Jalen Suggs","Franz Wagner","Cole Anthony"]
Kings=["Damontis Sabonis","Kevin Huerter","DeAaron Fox"]
Heat=["Jimmy Butler","Tyler Herro","Bam Adebayo"]
"""



"""
teamsPPGAverage={Timberwolves:{"Karl Anthony Towns":25,"Rudy Gobert": 18,"Anthony Edwards":29},
       Nets:{"Nic Claxton":15,"Cam Thomas":25,"seth curry":13},
       Clippers:{"Paul George":23,"Kawhi Leonard":14,"Marcus Morris":21},
       Magic:{"Jalen Suggs":19,"Franz Wagner":22,"Cole Anthony":12},
       Kings:{"Domantas Sabonis":28,"Kevin Huerter":8,"DeAaron Fox":22},
       Heat:{"Jimmy Butler":12,"Tyler Herro":9,"Bam Adebayo":20}}
"""

teamsWL={"Timberwolves":{"Wins":0,"Losses":0},"Nets":{"Wins":0,"Losses":0},"Clippers":{"Wins":0,"Losses":0},"Magic":{"Wins":0,"Losses":0},"Kings":{"Wins":0,"Losses":0},"Heat":{"Wins":0,"Losses":0}}

def play_game():
    while True:
        team1=input("Enter a team or type 'break' for both teams to quit: ")
        team2=input("Enter another team: ")
        team1Score=0
        team2Score=0
        if team1=="break":
            print(teamsWL)
            f=open("newFile.txt","w")
            f.write(str(teamsWL))
            f.close()
            break
        else:
            team1Score=random.randint(70,120)
            team2Score=random.randint(70,120)
            if team1Score > team2Score:
                teamsWL[team1]["Wins"] += 1
                teamsWL[team2]["Losses"]+=1
                print(team1Score,"-", team2Score)
                print(team1, "win!")
                print(teamsWL)
            else:
                teamsWL[team2]["Wins"] += 1
                teamsWL[team1]["Losses"] += 1
                print(team1Score, "-", team2Score)
                print(team2, "win!")
                print(teamsWL)

play_game()




''' 
import random

class BasketballPlayer:
    def __init__(self, name, team_name):
        self.name = name
        self.team_name = team_name
        self.score = 0  # initialize player's score to 0

    def play_game(self):
        self.score = random.randint(0, 50)  # simulate player's score using a random integer between 0 and 50

class BasketballGame:
    def __init__(self, my_team, opponent_team):
        self.my_team = my_team
        self.opponent_team = opponent_team

    def create_team(self):
        self.my_team = []
        for i in range(3):
            player_name = input(f"Enter player {i+1} name: ")
            self.my_team.append(BasketballPlayer(player_name, "My Team"))

    def play_game(self):
        print(f"My Team vs {self.opponent_team}")
        for player in self.my_team:
            player.play_game()  # simulate player's score
            opponent_player = random.choice(self.opponent_team)
            opponent_score = random.randint(0, 50)  # simulate opponent player's score
            print(f"{player.name} (My Team) scored {player.score} points vs {opponent_player} ({self.opponent_team}) scored {opponent_score} points")
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
game.play_game()'''
