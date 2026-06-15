import random

import json

import sys

Countrys = {"Brazil": 80, "Argentina": 88, "Spain": 70, "France": 77, "Netherlands": 90}

team1, team2 = random.sample(list(Countrys.keys()), k=2)

score1 = random.randint(1, 5)
score2 = random.randint(1, 5)


print("\nWorld cup Simulator!")
print(f"Match :\n{team1} vs {team2}\n")


try:
    if score1 == score2:

        print(f"Result:\n{team1} {score1} - {score2} {team2}")
        print("Match is a Draw!")

    elif score1 > score2:

        print(f"Result:\n{team1} {score1} - {score2} {team2}")
        print(f"{team1} Wins!")

    elif score1 < score2:
        print(f"Result:\n{team1} {score1} - {score2} {team2}")
        print(f"{team2} Wins!")

    else:
        print(f"Result:\n{team1} {score1} - {score2} {team2}")

except KeyError:
    sys.exit("Unable to find the team!")
