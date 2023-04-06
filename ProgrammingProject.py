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
teamsWL={"Timberwolves":{"Wins":0,"Losses":0},"Nets":{"Wins":0,"Losses":0},"Clippers":{"Wins":0,"Losses":0}}

while True:
    team1=input("Enter a team or type 'break' to quit: ")
    team2=input("Enter another team: ")
    team1Score=0
    team2Score=0
    if team1=="break":
        print(teamsWL)
        break
    else:
        team1Score=random.randint(70,120)
        team2Score=random.randint(70,120)
        if team1Score > team2Score:
            teamsWL[team1]["Wins"] += 1
            teamsWL[team2]["Losses"]+=1
            print(team1Score,"-", team2Score)
            print(teamsWL)
        else:
            teamsWL[team2]["Wins"] += 1
            teamsWL[team1]["Losses"] += 1
            print(team1Score, "-", team2Score)
            print(teamsWL)
              
              
              
              
              
              
              
              
              
              class BasketballGame:
    def __init__(self, opponent_team):
        self.opponent_team = opponent_team
        self.my_team = []

    def create_team(self):
        for i in range(3):
            player_name = input(f"Enter player {i+1} name: ")
            self.my_team.append(BasketballPlayer(player_name, "My Team"))

    def play_game(self):
        print(f"My Team vs {self.opponent_team}")
        for player in self.my_team:
            opponent_player = random.choice(self.opponent_team)
            print(f"{player.name} (My Team) vs {opponent_player} ({self.opponent_team})")
        print("Game result: My Team wins!")

# Pre-defined opponent teams
opponent_teams = {
    "Timberwolves": ["Karl Anthony-Towns", "Rudy Gobert", "Anthony Edwards"],
    "Nets": ["Nic Claxton", "Cam Thomas", "Seth Curry"],
    "Clippers": ["Paul George", "Kawhi Leonard", "Marcus Morris"],
    "Magic": ["Jalen Suggs", "Franz Wagner", "Cole Anthony"],
    "Kings": ["Damontis Sabonis", "Kevin Huerter", "DeAaron Fox"],
    "Heat": ["Jimmy Butler", "Tyler Herro", "Bam Adebayo"]
}

# Prompt the user to choose an opponent team
print("Choose an opponent team:")
for team_name in opponent_teams.keys():
    print(f"{team_name}")
choice = input("Enter team name: ")
opponent_team = opponent_teams[choice]

# Play the game
game = BasketballGame(opponent_team)
game.create_team()
game.play_game()
