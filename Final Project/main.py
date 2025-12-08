# Author: Divyang Parikh
# Date: 11/09/25
"""
Main Program – Journey to the Mysterious Island
Milestone 3 Final Project

This module starts the interactive fiction game based on
"Journey 2: The Mysterious Island".

It is responsible for:
- Showing the initial welcome banner.
- Asking the player for their name and creating the shared state dictionary.
- Running the main game loop that calls each chapter's play() function.
- Handling checkpoint labels returned from chapters to move the story forward.
"""

from utils import banner
from Chpt1 import play as ch1
from Chpt2 import play as ch2
from Chpt3 import play as ch3
from Chpt4 import play as ch4
from Chpt5 import play as ch5


def main():
    """
    Entry point for the Journey to the Mysterious Island game.

    The function:
    - Displays a welcome banner.
    - Prompts the player for their name and stores it in a shared state dict.
    - Uses a loop and checkpoint labels to move between chapters.
    - Ends the game once the player reaches a successful ending.
    """
    banner("Welcome to Journey to the Mysterious Island")

    # Ask player for their name; fallback to "Sean" if left blank.
    player_name = input("Enter your name: ").strip() or "Sean"
    print(f"\nWelcome, {player_name}! Your adventure begins now.\n")

    # Shared state dictionary passed to each chapter.
    # Chapters can read and update this dictionary as the story moves forward.
    state = {"player_name": player_name}

    # Start at the first chapter.
    current_chapter = "CH1"

    # Main game loop. Each chapter returns a checkpoint label that
    # decides which chapter runs next.
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
            # Player has finished with a successful ending.
            banner("🎉 CONGRATULATIONS 🎉")
            print(f"Well done, {player_name}! You and Grandpa escaped the island successfully!")
            print(f"Ending: {state.get('ending', 'Unknown')}")
            print("Thank you for playing Journey to the Mysterious Island!\n")
            break
        else:
            # Fallback in case a chapter returns an unknown label.
            print("Unknown checkpoint. Restarting game...\n")
            current_chapter = "CH1"


if __name__ == "__main__":
    main()
