from rich.prompt import Prompt

from player_stats import PlayerStats
from player_reader import PlayerReader

def print_players(choice, stats):
    print(f"Players in {choice}:")

    players = stats.top_scorers_by_nationality(choice)
    stats.print_table(players, choice)

def text_interface(nationalities, stats):
    while True:
        choice = input("input nationality (eg. FIN) or exit to exit: ")

        if choice == "exit":
            print("goodbye")
            break

        if choice not in nationalities:
            print("no players found")
            print()
            continue

        print_players(choice, stats)

def setup_season(reader):
    season = Prompt.ask(
        "Select season:",
        choices = reader.get_seasons(),
        default="2024-25"
    )

    return season

def main():
    url = 'https://studies.cs.helsinki.fi/nhlstats/'
    reader = PlayerReader(url)
    stats = PlayerStats(reader)

    season = setup_season(reader)

    stats.set_players(season)
    nationalities = stats.get_all_nationalities()

    text_interface(nationalities, stats)

if __name__ == "__main__":
    main()
