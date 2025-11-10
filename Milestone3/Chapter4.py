"""
Chapter 4 – Searching for the Submarine Bay
From Journey to the Mysterious Island
"""

from utils import banner, prompt_choice, checkpoint, restart_chapter


def play(state):
    banner("Chapter 4: Searching for the Submarine Bay")

    print("You and Grandpa head toward the island’s volcanic center. Tremors shake the ground,")
    print("steam erupts from cracks, and the air smells like sulfur.")
    print('Grandpa warns, "Sean, the island’s breaking apart faster than I thought. We have to move."\n')

    # Step 1: Choose the Route
    route = prompt_choice(
        "Which route will you take toward the volcano?",
        ["Ridge Path", "Tide Pools", "Lava Tubes", "Stay near camp to rest"]
    )

    if route == "ridge path":
        print("\nYou climb the narrow mountain trail. From above, you spot steam vents near the crater.")
        print("You mark their positions to guide you later.")
        state["vents_marker"] = True

    elif route == "tide pools":
        print("\nYou descend to the rocky shore. Timing the waves, you slip through an arch into a grotto.")
        print("The water-carved tunnel points inland toward a hidden bay.")
        state["secret_water_entry"] = True

    elif route == "lava tubes":
        print("\nYou crawl through scorching tunnels beneath the ground. The heat is intense.")
        print("On the wall you notice metal rails — signs of Nemo’s machinery.")
        state["mechanical_track"] = True

    else:  # Stay near camp to rest
        print("\nDark smoke fills the sky. The ground splits and molten rock bursts upward.")
        print("You’ve lost too much time. Mission Failed – Restart from Chapter 1.\n")
        return restart_chapter("CH1")

    # Step 2: Logical Check — Do you have enough information?
    print("\nDeeper in the tunnels, Grandpa stops you.")
    print('He says, "We can only reach the Nautilus Bay if we already have at least one real clue."')

    has_prior_clue = bool(
        state.get("passphrase") or state.get("map_to_bay") or state.get("nautilus_key")
    )

    if not has_prior_clue:
        print("\nWithout any solid clue, the mist and smoke disorient you. The tunnels loop back on themselves.")
        print("You’re forced to retreat as small collapses block the way.")
        print("Mission Failed – Restart from Chapter 4.\n")
        return restart_chapter("CH4_SEARCH")

    # Step 3: Success — Reach the Bay
    print("\nUsing your clues and the route markers, you navigate through a final passage.")
    print("A massive cavern opens up — glowing blue water reflects the metallic hull of the Nautilus.")
    print('Grandpa whispers, "We found it, Sean. Now we make her work."')
    return checkpoint("CH5_SUB")
