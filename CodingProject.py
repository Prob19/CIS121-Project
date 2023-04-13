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

teamsWL={"Timberwolves":{"Wins":0,"Losses":0, "Scores":[]},"Nets":{"Wins":0,"Losses":0, "Scores":[]},"Clippers":{"Wins":0,"Losses":0, "Scores":[]},"Magic":{"Wins":0,"Losses":0, "Scores":[]},"Kings":{"Wins":0,"Losses":0, "Scores":[]},"Heat":{"Wins":0,"Losses":0, "Scores":[]}}

def play_game():
    while True:
        team1 = input("Enter a team or type 'break' for both teams to quit: ")
        team2 = input("Enter another team: ")
        team1Score = 0
        team2Score = 0
        if team1 == "break":
            print(teamsWL)
            with open("newFile.txt", "w") as f:
                f.write(str(teamsWL))
            break
        else:
            team1Score = random.randint(70, 120)
            team2Score = random.randint(70, 120)
            if team1Score > team2Score:
                teamsWL[team1]["Wins"] += 1
                teamsWL[team2]["Losses"] += 1
                print(team1Score, "-", team2Score)
                print(team1, "win!")
            else:
                teamsWL[team2]["Wins"] += 1
                teamsWL[team1]["Losses"] += 1
                print(team1Score, "-", team2Score)
                print(team2, "win!")
            # Add scores to teamsWL
            teamsWL[team1]["Scores"].append(team1Score)
            teamsWL[team2]["Scores"].append(team2Score)
		
def calculate_ppg(teamsWL):
    for team in teamsWL:
        games_played = teamsWL[team]['Wins'] + teamsWL[team]['Losses']
        if games_played == 0:
            ppg = 0
        else:
            total_score = 0
            for score in teamsWL[team]['Scores']:
                total_score += score
            ppg = total_score / games_played
        print(f"{team}: {ppg}")

# Define teamsWL and call play_game() to simulate games
teamsWL = {"Timberwolves": {"Wins": 0, "Losses": 0, "Scores": []},
           "Nets": {"Wins": 0, "Losses": 0, "Scores": []},
           "Clippers": {"Wins": 0, "Losses": 0, "Scores": []},
           "Magic": {"Wins": 0, "Losses": 0, "Scores": []},
           "Kings": {"Wins": 0, "Losses": 0, "Scores": []},
           "Heat": {"Wins": 0, "Losses": 0, "Scores": []}}

play_game()

# Call calculate_ppg() to calculate each team's points per game average
calculate_ppg(teamsWL)
