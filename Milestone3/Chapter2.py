"""
Chapter 2 – Crash Landing and Giant Creatures
From Journey to the Mysterious Island
"""

from utils import banner, prompt_choice, checkpoint, restart_chapter


def play(state):
    banner("Chapter 2: Crash Landing and Giant Creatures")

    print("You and the pilot crash-land on the mysterious island after surviving the storm.")
    print("The helicopter is destroyed, but you are alive. The island looks unreal—")
    print("tiny elephants walk near your feet, and giant lizards move in the distance.\n")

    # Step 1: Exploration After Crash
    choice1 = prompt_choice(
        "What will you do first?",
        ["Explore carefully", "Wander carelessly", "Stay near helicopter"]
    )

    if choice1 == "explore carefully":
        print("You move cautiously through the jungle and find edible fruits and fresh water.")
        state["has_food"] = True
    elif choice1 == "wander carelessly":
        print("You step into a lizard’s territory and it notices you!")
        state["has_food"] = False
    else:
        print("Night falls while you stay near the helicopter. Strange noises approach.")
        print("Mission Failed – Restart from Chapter 2.\n")
        return restart_chapter("CH2_CRASH")

    # Step 2: Encounter with the Giant Lizard
    print("\nA giant lizard blocks your path, its scales reflecting sunlight like armor.")
    choice2 = prompt_choice(
        "How will you react?",
        ["Fight", "Escape", "Distract"]
    )

    if choice2 == "fight":
        print("You swing a stick at the lizard, but it barely flinches.")
        print("Mission Failed – Restart from Chapter 2.\n")
        return restart_chapter("CH2_CRASH")

    elif choice2 == "escape":
        print("You sprint through the trees, diving behind thick roots until you lose the creature.")
        print("You find a steep path leading toward the mountain. The air hums faintly above.\n")
        return checkpoint("CH3_GRANDPA")

    else:  # Distract
        print("You throw your bag filled with snacks. The lizard stops to eat, giving you time to run.")
        print("You reach a high ridge where the forest clears, revealing a distant hut inland.\n")
        state["lost_supplies"] = True
        return checkpoint("CH3_GRANDPA")
