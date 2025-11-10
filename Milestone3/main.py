"""
Main Program – Journey to the Mysterious Island
Milestone 3 Final Project
"""

from utils import banner
from Chapter1 import play as ch1
from Chapter2 import play as ch2
from Chapter3 import play as ch3
from Chapter4 import play as ch4
from Chapter5 import play as ch5


def main():
    banner("Welcome to Journey to the Mysterious Island")

    player_name = input("Enter your name: ").strip() or "Sean"
    print(f"\nWelcome, {player_name}! Your adventure begins now.\n")

    state = {"player_name": player_name}

    current_chapter = "CH1"

    # Game loop
    while True:
        if current_chapter == "CH1":
            current_chapter = ch1(state)
        elif current_chapter == "CH2_CRASH":
            current_chapter = ch2(state)
        elif current_chapter == "CH3_GRANDPA":
            current_chapter = ch3(state)
        elif current_chapter == "CH4_SEARCH":
            current_chapter = ch4(state)
        elif current_chapter == "CH5_SUB":
            current_chapter = ch5(state)
        elif current_chapter == "END_SUCCESS":
            banner("🎉 CONGRATULATIONS 🎉")
            print(f"Well done, {player_name}! You and Grandpa escaped the island successfully!")
            print(f"Ending: {state.get('ending', 'Unknown')}")
            print("Thank you for playing Journey to the Mysterious Island!\n")
            break
        else:
            print("Unknown checkpoint. Restarting game...\n")
            current_chapter = "CH1"


if __name__ == "__main__":
    main()
