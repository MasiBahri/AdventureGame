import time
import random

weapon = []
creature = ""


def print_pause(sentence):
    # print given message and a break after
    print(sentence)
    time.sleep(0.52)


def choose_creature():
    # choose a creature randomly
    global creature
    creature = random.choice(["pirate", "dragon", "dinosaur", "murderer"])


def intro():
    # introduction
    print_pause("You find yourself standing in a jungle,"
                " full of tall trees and bush and prickly plants.")
    print_pause("Rumor has it that a " + creature + " is"
                                                    " somewhere around here "
                                                    " and has killed some kids"
                                                    " in the village.")
    print_pause("In front of you is an old castle")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand, you hold a dagger.")


def castle_or_cave():
    # choose one way between castle and cave
    print_pause("Enter 1 to knock on the door of the castle.")
    print_pause("Enter 2 to peer into the cave.")
    while True:
        path = input("What would you like to do? Please enter 1 or 2.\n")
        if "1" in path:
            castle()
            break
        elif "2" in path:
            cave()
            break
        else:
            type_correctly()


def castle():
    # describe what happen in the castle
    print_pause("You approach the door of the castle.")
    print_pause("You are about to knock when the door opens"
                " and out steps a " + creature + ".")
    print_pause("Eep! This is the " + creature + "'s castle!")
    print_pause("The " + creature + " attacks"
                                    " you!")
    print_pause("You feel unprepared for this,"
                " what with only having a tiny dagger.")
    while True:
        decision_in_castle = input("Would you like to (1)"
                                   " fight or (2) run away?\n")
        if "1" in decision_in_castle:
            if "sword" in weapon:
                print_pause("As the " + creature + " moves to attack,"
                                                   " you unsheath new sword.")
                print_pause("The Sword of Ogoroth shines brightly in your hand"
                            " as you brace yourself for the attack.")
                print_pause("But the " + creature + " takes"
                                                    " one look at your shiny"
                                                    " new toy and runs away!")
                print_pause("You have rid the town of"
                            " the " + creature + "You are VICTORIOUS!")
                play_again()
            else:
                print_pause("You do your best...")
                print_pause("but your dagger is no match for"
                            " the " + creature + ".")
                print_pause("You have been DEFEATED!")
                print_pause('"GAME OVER"')
                play_again()
            break
        elif "2" in decision_in_castle:
            print_pause("You run back into the jungle.")
            print_pause("Luckily, you don't seem to have been followed.")
            castle_or_cave()
            break
        else:
            type_correctly()


def cave():
    # describe what happen in the cave
    global weapon
    print_pause("You peer cautiously into the cave.")
    if "sword" in weapon:
        print_pause("You've been here before, and gotten all the good stuff."
                    " It's just an empty cave now.")
    else:
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical Sword of Ogoroth!")
        print_pause("You discard your dagger and take the sword with you.")
        weapon.append("sword")
    print_pause("You walk back out to the jungle.")
    castle_or_cave()


def play_again():
    # user can chose between continuing game or not
    question = input("Would you like to play again? (y/n)\n").lower()
    if "y" in question:
        adventure_game()
    elif "n" in question:
        print_pause("Thanks for playing!")
        print_pause("See you next time.")
    else:
        type_correctly()
        play_again()


def type_correctly():
    # tell to the user that type correct input
    print_pause("You have typed a wrong input.")
    print_pause("Please type again")


def adventure_game():
    choose_creature()
    intro()
    castle_or_cave()


if __name__ == '__main__':
    adventure_game()
