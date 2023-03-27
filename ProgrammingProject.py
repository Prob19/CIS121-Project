import random
Timberwolves=["Karl Anthony-Towns","Rudy Gobert","Anthony Edwards"]
Nets=["Nic Claxton","Cam Thomas","Seth Curry"]
Clippers=["Paul George","Kawhi Leonard","Marcus Morris"]
Magic=["Jalen Suggs","Franz Wagner","Cole Anthony"]
Kings=["Damontis Sabonis","Kevin Huerter","DeAaron Fox"]
Heat=["Jimmy Butler","Tyler Herro","Bam Adebayo"]




teams={Timberwolves:{"Karl Anthony Towns":25,"Rudy Gobert": 18,"Anthony Edwards":29},
       Nets:{"Nic Claxton":15,"Cam Thomas":25,"seth curry":13},
       Clippers:{"Paul George":23,"Kawhi Leonard":14,"Marcus Morris":21},
       Magic:{"Jalen Suggs":19,"Franz Wagner":22,"Cole Anthony":12},
       Kings:{"Domantas Sabonis":28,"Kevin Huerter":8,"DeAaron Fox":22},
       Heat:{"Jimmy Butler":12,"Tyler Herro":9,"Bam Adebayo":20}}

def simulateGame(team1,team2):
    team1Score=random.randint(0,100)
    team2Score=random.randint(0,100)
    if team1Score > team2Score:
        
