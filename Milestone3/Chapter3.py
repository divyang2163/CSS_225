"""
Chapter 3 – Grandpa, Treasure, and Bird Attack
From Journey to the Mysterious Island
"""

from utils import banner, prompt_choice, checkpoint, restart_chapter


def play(state):
    banner("Chapter 3: Grandpa, Treasure, and Bird Attack")

    print("After escaping the jungle, you follow a rocky path up the mountain.")
    print("Through the mist, you spot smoke coming from a small hut. Inside, you finally find your grandpa!")
    print("He tells you the island is sinking and the only way to escape is by finding Captain Nemo's submarine, the Nautilus.")
    print("To activate it, you must locate three clues hidden across the island: a passphrase, a map, and a key.\n")

    # Step 1: Searching for the Clues
    choice1 = prompt_choice(
        "Where will you search for a clue?",
        ["Beach Cave", "Old Outpost", "Forest Shrine", "Ignore clues and rest"]
    )

    if choice1 == "beach cave":
        print("\nYou trek toward the shoreline and crawl through glowing coral tunnels.")
        print("At the end, you find a brass plate covered in barnacles.")
        print("When you clean it, the words appear: 'Heart of Fire'. You take it with you.")
        state["passphrase"] = "heart of fire"

    elif choice1 == "old outpost":
        print("\nYou climb a steep cliff to an abandoned camp filled with old journals and broken tools.")
        print("Among the clutter, you discover a map showing a safe route to the volcanic bay.")
        state["map_to_bay"] = True

    elif choice1 == "forest shrine":
        print("\nYou cross a swaying bridge deep in the jungle and reach a mossy statue.")
        print("In its stone hands rests a rusted key engraved with the Nautilus emblem.")
        state["nautilus_key"] = True

    else:
        print("\nYou decide to rest instead of searching. By morning, the rain has washed away the trails.")
        print("Grandpa is nowhere to be found. Mission Failed – Restart from Chapter 1.\n")
        return restart_chapter("CH1")

    # Step 2: Giant Bird Attack (happens during exploration)
    print("\nAs you study your discovery, the sky darkens and the ground trembles.")
    print("A deafening screech echoes through the air – giant birds swoop down from the cliffs!")

    choice2 = prompt_choice(
        "What do you do as the birds attack?",
        ["Hide under roots", "Wave torch", "Throw rocks"]
    )

    if choice2 == "hide under roots":
        print("\nYou dive under thick jungle roots and stay completely still.")
        print("The birds shriek above but soon fly away. You survive unharmed.")
    elif choice2 == "wave torch":
        print("\nYou light a small torch and wave it wildly. The smoke scares the birds away,")
        print("but you drop some of your supplies in the process.")
        state["lost_supplies"] = True
    else:  # Throw rocks
        print("\nYou grab a rock and throw it, but the birds are too fast!")
        print("One dives at you, knocking you down a slope and into the mud.")
        print("Mission Failed – Restart from Chapter 3.\n")
        return restart_chapter("CH3_GRANDPA")

    # Step 3: End of Chapter
    print("\nAs the sky clears, you carefully return to Grandpa’s hut with your clue in hand.")
    print("He examines it and smiles, saying, 'We’re close now. Tomorrow we enter the tunnels below the volcano.'")
    print("You prepare your supplies for the next stage of your adventure.\n")

    return checkpoint("CH4_SEARCH")
