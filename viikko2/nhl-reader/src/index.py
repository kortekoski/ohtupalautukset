from player import Player
from player_stats import PlayerStats
from player_reader import PlayerReader

from rich.prompt import Prompt
from rich import print
import requests

def main(): 
    url = 'https://studies.cs.helsinki.fi/nhlstats/'
    reader = PlayerReader(url)
    stats = PlayerStats(reader)

    print(reader.get_seasons())

    season = Prompt.ask(
        "Select season:",
        choices = reader.get_seasons(),
        default="2024-25"
    )

    stats.set_players(season)
    nationalities = stats.get_all_nationalities()

    while(True):
        choice = input("input nationality (eg. FIN) or exit to exit: ")

        if choice == "exit":
            print("goodbye")
            break

        if choice not in nationalities:
            print("no players found")
            print()
            continue

        print(f"Players in {choice}:")

        players = stats.top_scorers_by_nationality(choice)
        stats.print_table(players, choice)

if __name__ == "__main__":
    main()
