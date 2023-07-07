import random

def get_options_string(options):
    return ", ".join([f"[{key.upper()}]{value[1:]}" for key, value in options.items()])

def choose_weapon():
    options = {"l": "Lightsaber", "b": "Blaster", "f": "Force"}
    rebel_choice = ""
    error_message = False
    
    while rebel_choice not in options.keys():
        if not error_message:
            rebel_choice = input("\nAs a Rebel Jedi, you encounter an enemy Imperial Warrior!\nWhat weapon will you chose?\n" + get_options_string(options) + "\n").lower()
        else:
            rebel_choice = input(get_options_string(options) + "\n").lower()
        
        if rebel_choice not in options.keys():
            if not error_message:
                print(f"\nRemember Master Yoda's teaching...\nValid input you must give, young padawan!\nEither 'L', 'B', or 'F' it should be. There is no '{rebel_choice}'.")
                error_message = True

    rebel_choice = options[rebel_choice]
    imperial_choice = random.choice(list(options.values()))
    choices = {"Rebel Jedi": rebel_choice, "Imperial Warrior": imperial_choice}
    return choices

def check_victor(rebel, imperial):
    print (f"\nRebel Jedi chose {rebel}, and Imperial Warrior chose {imperial}.")

    if rebel == imperial:
        return "\nIt's a draw, the battle continues!"
    elif rebel == "Lightsaber": 
        if imperial == "Blaster":
            return "\nLightsaber deflects Blasters!\nYou did it! Because of you the rebels won the fight!"
        else:
            return "\nThe Force controls the Lightsaber!\nThe Empire has crushed the Rebellion!"
    elif rebel == "Blaster": 
        if imperial == "Force":
            return "\nBlaster destroys the Force!\nYou did it! Because of you the rebels won the fight!"
        else:
            return "\nLightsaber deflects Blasters!\nThe Empire has crushed the Rebellion!"
    elif rebel == "Force": 
        if imperial == "Lightsaber":
            return "\nThe Force controls the Lightsaber!\nYou did it! Because of you the rebels won the fight!"
        else:
            return "\nBlaster destroys the Force!\nThe Empire has crushed the Rebellion!"

def continue_battle():
    while True:
        choices = choose_weapon()
        result = check_victor(choices["Rebel Jedi"], choices["Imperial Warrior"])
        print(result)

        play_again = ""
        options = {"y": "Yes", "n": "No"}
        error_message = False
        
        while play_again not in options.keys():
            if not error_message:
                if "won" in result:
                    play_again = input("\nHan Solo turns to you and says\nGreat, kid! Don't get cocky.\nShall we continue the battle, kid?\n" + get_options_string(options) + "\n").lower()
                else:
                    play_again = input("\nObi-Wan appears from the force itself and says\n'The Force will be with you. Always.\nDo you want to continue and bring balance to the universe?\n" + get_options_string(options) + "\n").lower()
            else:
                play_again = input(get_options_string(options) + "\n").lower()

            if play_again not in options.keys() and not error_message:
                print(f"\nRemember Master Yoda's teaching...\nEither 'Y', 'N', or their full words, it should be. There is no '{play_again}'.")
                error_message = True

        if play_again.startswith("n"):
            break

continue_battle()
