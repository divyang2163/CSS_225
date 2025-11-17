# Name: Divyang Parikh
# Date: 11/15/2025
# Program 5: Checks if a character can perform tasks based on items + weaknesses

class character:
    def __init__(self, nickname, weapons, weaknesses):
        self.nickname = nickname              # character name
        self.weapons = weapons                # list of items the character has
        self.weaknesses = weaknesses          # list of debuffs the character has


# Creating the game character with required items and weaknesses
player1 = character(
    nickname="Dragon Slayer",
    weapons=['pan', 'paper', 'idea', 'rope', 'groceries'],   # items given in assignment
    weaknesses=['slow']                                      # weakness given in assignment
)


def can_climb_mountain(player):
    needed = {'rope', 'coat', 'first aid kit'}               # required items for task

    # Check if all needed items are present
    if not needed.issubset(player.weapons):
        print("Cannot climb mountain: missing required items.")
        return False

    # Check if player has slow debuff
    if "slow" in player.weaknesses:
        print("Cannot climb mountain: you are slowed.")
        return False

    print("You can climb the mountain!")
    return True


def can_cook_meal(player):
    needed = {'pan', 'groceries'}                            # required items for cooking

    if not needed.issubset(player.weapons):
        print("Cannot cook: missing required items.")
        return False

    # Cannot have "small" debuff (as per assignment)
    if "small" in player.weaknesses:
        print("Cannot cook: you have the 'small' debuff.")
        return False

    print("You can cook a meal!")
    return True


def can_write_book(player):
    needed = {'pen', 'paper', 'idea'}                        # required items for writing a book

    if not needed.issubset(player.weapons):
        print("Cannot write a book: missing required items.")
        return False

    if "confusion" in player.weaknesses:
        print("Cannot write: character is confused.")
        return False

    print("You can write a book!")
    return True

#Test Run

print("---- Task 1: Climb Mountain ----")
can_climb_mountain(player1)

print("\n---- Task 2: Cook Meal ----")
can_cook_meal(player1)

print("\n---- Task 3: Write Book ----")
can_write_book(player1)
