import easygui

# Card lists to store each card and each of their corresponding value.
cards = {
    'Stoneling': {
        'Strength': 7,
        'Speed': 1,
        'Stealth': 25,
        'Cunning': 15
    },

    'Vexscream': {
        'Strength': 1,
        'Speed': 6,
        'Stealth': 21,
        'Cunning': 19
    },

    'Dawnmirage': {
        'Strength': 5,
        'Speed': 15,
        'Stealth': 18,
        'Cunning': 22
    },

    'Blazegolem': {
        'Strength': 15,
        'Speed': 20,
        'Stealth': 23,
        'Cunning': 6
    },

    'Websnake': {
        'Strength': 7,
        'Speed': 15,
        'Stealth': 10,
        'Cunning': 5
    },

    'Moldvine': {
        'Strength': 21,
        'Speed': 18,
        'Stealth': 14,
        'Cunning': 5
    },

    'Vortexwing': {
        'Strength': 19,
        'Speed': 13,
        'Stealth': 19,
        'Cunning': 2
    },

    'Rotthing': {
        'Strength': 16,
        'Speed': 7,
        'Stealth': 4,
        'Cunning': 12
    },

    'Froststep': {
        'Strength': 14,
        'Speed': 14,
        'Stealth': 17,
        'Cunning': 4
    },

    'Wispghoul': {
        'Strength': 17,
        'Speed': 19,
        'Stealth': 3,
        'Cunning': 2
    }

}

# Display the all the cards and their values when the user uses the Display button.
def display_menu():
    # If there is no card in the card lists, print the text "There is no cards available to display. Maybe try to add one?"
    if not cards:
        easygui.msgbox("There is no cards available to display.\n\nMaybe try to add one?")
        # Return back to the main page (Main function)
        return
    
    # This is the place where the information (eg., card names and their values) will be stored in.
    text = ""
    # Scan for every card and its value.
    for name, ability in cards.items():
        # Store and print the card's name.
        text += f"\n[{name}]:\n"
        # Print the card's value along with its name.
        for ability, value in ability.items():
            # Store the abilities into the 'text' variable below.
            text += f"{ability} - {value}\n"

    # Use Easygui message box to print out all the stored information from 'text' in an interface.
    easygui.msgbox(text, title = "DISPLAY MENU")
