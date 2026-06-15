import random

import json

import sys

Countrys={"Brazil":90,
       "Argentina":88,


}

def main():
    score1=random.randint(1,5)
    score2=random.randint(2,4)
    teams=random.choices(list(Countrys.keys()),weights=list(Countrys.values()))
    for team in teams:
        
        if score1==score2:
            print(f"Match is a draw between Argentina & Brazil  {score1} - {score2}")
        elif score1>score2:
            print(f"{team} Has won {score1} - {score2}")
        elif score1<score2:
            print(f"{team} Has won {score2} - {score1}")
        else:
            print(f"{team} Has won {score1} - {score2}")
main()




