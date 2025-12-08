# Author: Divyang Parikh
# Date: 11/09/25
"""
Chapter 1 – The Message and the Flight
From Journey to the Mysterious Island

This chapter introduces the main conflict of the story. The player receives
a mysterious coded message about their missing grandpa and a hidden island.
The player must:

1. Decode the message.
2. Find a pilot.
3. Survive a dangerous helicopter flight through a storm.

State keys updated in this chapter:
- "coords" (bool): True if the coordinates are decoded perfectly.
- "pilot_help" (bool): True if a pilot agrees to help.

Possible checkpoints returned:
- "CH2_CRASH": Player reaches the island and moves to Chapter 2.
- "Chapter1": Restart label used when the player fails this chapter.
"""

from utils import banner, prompt_choice, checkpoint, restart_chapter


def play(state):
    """
    Run the interactive events for Chapter 1.

    Args:
        state (dict): Shared game state with information like "player_name".

    Returns:
        str: A checkpoint label that tells the main loop which chapter comes next.
    """
    banner("Chapter 1: The Message and the Flight")

    # Get player name from shared state, default to "Sean" if not set.
    player = state.get("player_name", "Sean")
    print(
        f"{player} receives a mysterious coded message about his missing grandpa "
        "and a hidden island surrounded by storms."
    )
    print("To reach it, you must decode the message, find a pilot, and survive the flight.\n")

    # Step 1: Decode the Message
    choice1 = prompt_choice(
        "How will you decode the message?",
        ["Use frequency scanner", "Guess pattern", "Give up"]
    )

    if choice1 == "use frequency scanner":
        print("You analyze the signal and decode the coordinates perfectly.")
        state["coords"] = True
    elif choice1 == "guess pattern":
        print("You manage to get rough coordinates, but some data may be missing.")
        state["coords"] = False
    else:
        # Player chooses to give up early. They must restart the chapter.
        print("You quit too early. Mission Failed – Restart from Start.\n")
        return restart_chapter("Chapter1")

    # Step 2: Find a Pilot
    print("\nNow you need a pilot brave enough to fly near the storm zone.")
    choice2 = prompt_choice(
        "What will you do to find one?",
        ["Offer payment and plan", "Plead emotionally", "Fail to find anyone"]
    )

    if choice2 == "offer payment and plan":
        print("Your determination and plan convince a pilot to join you.")
        state["pilot_help"] = True
    elif choice2 == "plead emotionally":
        print("The pilot hesitates but agrees after hearing your story.")
        state["pilot_help"] = True
    else:
        # No pilot means the story cannot continue.
        print("No pilot agrees to go. Mission Failed – Restart from Start.\n")
        return restart_chapter("Chapter1")

    # Step 3: Helicopter Flight and Storm
    print("\nYou and the pilot take off toward the island coordinates.")
    print("Dark clouds surround the helicopter as lightning flashes across the sky.")

    choice3 = prompt_choice(
        "What will you do as the storm hits?",
        ["Follow pilot instructions", "Panic and ignore directions"]
    )

    if choice3 == "follow pilot instructions":
        print(
            "You steer perfectly with the pilot’s guidance and land safely "
            "on the mysterious island!"
        )
        # Successful arrival at the island leads to Chapter 2.
        return checkpoint("CH2_CRASH")
    else:
        print("You lose control and crash into the waves below.")
        print("Mission Failed – Restart from Start.\n")
        return restart_chapter("Chapter1")
