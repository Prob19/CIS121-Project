from CodingProject import*

# Define teamsWL and call play_game() to simulate games
teamsWL = {"Timberwolves": {"Wins": 0, "Losses": 0, "Scores": []},
           "Nets": {"Wins": 0, "Losses": 0, "Scores": []},
           "Clippers": {"Wins": 0, "Losses": 0, "Scores": []},
           "Magic": {"Wins": 0, "Losses": 0, "Scores": []},
           "Kings": {"Wins": 0, "Losses": 0, "Scores": []},
           "Heat": {"Wins": 0, "Losses": 0, "Scores": []}}


play_game()

# Call calculate_ppg() to calculate each team's points per game average
calculate_ppg()
