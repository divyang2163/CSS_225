"""
Chapter 5 – Fixing the Submarine and Escape
From Journey to the Mysterious Island
"""

from utils import banner, prompt_choice, checkpoint, restart_chapter


def play(state):
    banner("Chapter 5: Fixing the Submarine and Escape")

    print("You and Grandpa enter the glowing underground cavern that holds the Nautilus.")
    print("Steam hisses through the cracks while blue light reflects off the metal hull.")
    print("The volcano rumbles louder with every passing minute — time is running out!\n")

    # Step 1: Opening the Submarine Panel
    print("You climb aboard the Nautilus and reach the main control hatch.")
    choice1 = prompt_choice(
        "How will you open the panel?",
        ["Use Nautilus Key", "Bypass wiring manually", "Force panel open", "Wait for Grandpa to do it"]
    )

    if choice1 == "use nautilus key":
        if state.get("nautilus_key"):
            print("\nThe key fits perfectly. The hatch unlocks with a metallic click.")
        else:
            print("\nYou don't have the key! The attempt fails. Mission Failed – Restart from Chapter 5.\n")
            return restart_chapter("CH5_SUB")

    elif choice1 == "bypass wiring manually":
        print("\nYou strip the old wires and connect them by hand. Sparks fly, but the hatch pops open.")
        state["panel_opened"] = True

    elif choice1 == "force panel open":
        print("\nYou pull the lever with all your strength — it snaps in half.")
        print("The door jams completely. Mission Failed – Restart from Chapter 5.\n")
        return restart_chapter("CH5_SUB")

    else:  # Wait for Grandpa
        print("\nYou wait for Grandpa to handle it, but the ground begins to shake violently.")
        print("The lava bursts into the cavern before you can react.")
        print("Mission Failed – Restart from Chapter 1.\n")
        return restart_chapter("CH1")

    # Step 2: Activating the Power System
    print("\nInside the Nautilus, dim lights flicker as ancient machinery hums to life.")
    print("A robotic voice echoes: 'Enter activation phrase to start primary engines.'")

    choice2 = prompt_choice(
        "What phrase will you say?",
        ["Heart of Fire", "Calm Seas", "Stay silent"]
    )

    if choice2 == "heart of fire":
        if state.get("passphrase") == "heart of fire":
            print("\nThe engines roar to life, gauges light up, and the Nautilus begins to awaken!")
            state["engines_on"] = True

    elif choice2 == "calm seas":
        print("\nThe system buzzes. 'Incorrect phrase detected.'")
        print("A short circuit shuts down the main controls.")
        print("Mission Failed – Restart from Chapter 5.\n")
        return restart_chapter("CH5_SUB")

    else:  # Stay silent
        print("\nThe timer on the screen reaches zero.")
        print("The engines fail to start, and lava begins flooding the bay.")
        print("Mission Failed – Restart from Chapter 1.\n")
        return restart_chapter("CH1")

    # Step 3: Escaping the Island
    print("\nThe Nautilus hums, its lights brightening as power stabilizes.")
    print("Grandpa shouts, 'Sean, the tunnel’s collapsing! Choose an exit now!'\n")

    choice3 = prompt_choice(
        "Which path will you take?",
        ["Sea Tunnel", "Vent Shaft", "Wait inside the bay"]
    )

    if choice3 == "sea tunnel":
        print("\nYou guide the Nautilus through narrow rock walls as the volcano collapses behind you.")
        print("Moments later, you burst into open ocean. The sky glows with the last eruption of the island.")
        print("Grandpa smiles and says, 'We made it, Sean. The island’s gone, but we’re alive.'")
        state["ending"] = "Perfect Escape through the Sea Tunnel"
        return checkpoint("END_SUCCESS")

    elif choice3 == "vent shaft":
        print("\nYou steer toward the upper vents. Lava bursts follow you, but the Nautilus endures.")
        print("You surface near the ridge, coughing through the steam — but you survived!")
        state["ending"] = "Alternate Escape through the Vent Shaft"
        return checkpoint("END_SUCCESS")

    else:  # Wait inside the bay
        print("\nYou hesitate as Grandpa yells for you to move.")
        print("A moment later, molten lava floods the cavern and engulfs the Nautilus.")
        print("Mission Failed – Restart from Chapter 1.\n")
        return restart_chapter("CH1")
