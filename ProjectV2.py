import random

teamsWL={"Timberwolves":{"Wins":0,"Losses":0},"Nets":{"Wins":0,"Losses":0},"Clippers":{"Wins":0,"Losses":0},"Magic":{"Wins":0,"Losses":0},"Kings":{"Wins":0,"Losses":0},"Heat":{"Wins":0,"Losses":0}}




class BasketballGame:
    def __init__(self, opponent_team):
        self.opponent_team = opponent_team
        self.my_team = []

    def create_team(self):
        for i in range(3):
            player_name = input("Enter player name: ")
            self.my_team.append(player_name)
            i += 1

    def play_game(self,team2):
        print(f"My Team vs {self.opponent_team}")
        myteamScore = 0
        team2Score = 0
        myteamScore = random.randint(70, 120)
        team2Score = random.randint(70, 120)
        if myteamScore > team2Score:
            teamsWL[self.my_team]["Wins"] += 1
            teamsWL[self.opponent_team]["Losses"] += 1
            print(myteamScore, "-", team2Score)
            print(myteamScore, "win!")
            print(teamsWL)
        else:
            teamsWL[team2]["Wins"] += 1
            teamsWL[myteamScore]["Losses"] += 1
            print(myteamScore, "-", team2Score)
            print(team2, "win!")
            print(teamsWL)


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