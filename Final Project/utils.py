# Author: Divyang Parikh
# Date: 11/09/25
"""
Utility functions for the Journey to the Mysterious Island game.

This module contains small helper functions that keep the chapter files
clean and focused on story content:

- banner(title): Prints a decorated title banner for chapters and game messages.
- prompt_choice(question, options): Asks the player to choose from a list of options
  and validates their input.
- checkpoint(label): Returns a label that the main game loop uses to decide
  which chapter to load next.
- restart_chapter(label): Prints a restart message and returns the label of
  the chapter that should be replayed.
"""


def banner(title):
    """
    Print a simple text banner with the given title.

    Args:
        title (str): The message or chapter name to display.
    """
    print("=" * 60)
    print(title)
    print("=" * 60)


def prompt_choice(question, options):
    """
    Ask the player a question with multiple fixed options and return their choice.

    The function keeps asking until the player types a valid option, ignoring case.

    Args:
        question (str): The text of the question to show the player.
        options (list[str]): A list of valid string options.

    Returns:
        str: The option that the player selected, always in lowercase.
    """
    print(question)
    print("Options:", ", ".join(options))

    # Normalize user input and the valid options so we can compare in lowercase.
    ans = input("> ").strip().lower()
    valid = [o.lower() for o in options]

    # Loop until the user types a valid choice.
    while ans not in valid:
        print("Please choose one of:", ", ".join(options))
        ans = input("> ").strip().lower()

    return ans


def checkpoint(label):
    """
    Return a checkpoint label that tells the main loop which chapter to run next.

    Args:
        label (str): A string identifier like "CH2_CRASH" or "END_SUCCESS".

    Returns:
        str: The same label, passed back to the main game loop.
    """
    return label


def restart_chapter(label):
    """
    Print a restart message and return a label for the chapter to replay.

    Args:
        label (str): A string identifier for the chapter that should restart.

    Returns:
        str: The label that the main loop will use on the next iteration.
    """
    print("Restarting chapter...")
    return label
