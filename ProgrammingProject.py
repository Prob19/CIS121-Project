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
class Players:
    def __init__(self, name):
       self.name = name

    def __add__(self, other):
     return Players(self.name + " " + other.name)
    
    def __str__(self):
       return f"Player Name: {self.name}"
    
    def add_player_name(self):
       player_name = input("Please enter a player name:")
       self.name += " " + player_name
obj = Players("New Player:")
print(obj)
obj.add_player_name()
print(obj)
