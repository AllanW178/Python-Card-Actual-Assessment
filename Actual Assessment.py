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

# Search menu function; this allowed users to search cards with some interactable buttons.
def search_menu():
    # If there is no card in the card lists, print the text "There is no cards available to display.".
    if not cards:
        easygui.msgbox("There is no cards available to search.", title = "NOTE")
        return

    # Here are the options/buttons for the user to choose and search them.
    search_card = easygui.buttonbox("Choose an option below to search:", title = "SEARCH PAGE", choices = list(cards.keys()))

    # Check if the chosen card is in the card list.
    if search_card in cards:
        # Store the chosen card's name and print out the card's name that the user chose to search.
        text = f"\n[{search_card}]:\n"
        # For every card name, and ability in the cards:
        for card_names, abilities in cards[search_card].items():
            # Add the information into the 'text' and print out them in the Easygui later.
            text += f"{card_names} - {abilities}\n"
    
    # Print out the stored 'text' in the Easygui with a title of 'SEARCH RESULT'.
    easygui.msgbox(text, title = "SEARCH RESULT")


# This is the function to remove any cards if needed.
def remove_menu():
    # If the system detects no cards available in the card list, it will print 'There is no cards available to remove.'.
    if not cards:
        easygui.msgbox("There is no cards available to remove.", title = "NOTE")
        return
    
    # The line below will provide the buttons for the user to utilise. For example, if the user wants remove card '1', they can do so by clicking the button.
    remove_card = easygui.buttonbox("Choose an option below to remove:", title = "REMOVE PAGE", choices = list(cards.keys()))

    # If the chosen card is detected in the card list, it is going to be removed.
    if remove_card in cards:
        del cards[remove_card]
    
    # Print out the success message when the chosen card has been removed in the interface.
    easygui.msgbox(f"{remove_card} has been successfully removed!", title = "SUCCESS")

# This is a main menu, the user can manipulate all the functions here (eg., Display Card, Search Card, Remove Card, Add Card, Modify Card & Exit the program).
def main():
    # A while loop so the program will keep going until the user interacts with the '[EXIT]' button.
    while True:
        # The line below are the main buttons for the user to control. For example, it's up to the user whether he/she wants to use Display Card, Search Card, or etc.
        choice = easygui.buttonbox("Choose an option below:", title = "MAIN MENU", choices = ["Display Card", "Search Card", "Remove Card", "Add Card", "Edit Card", '[EXIT]'])

        # Check if the choice is Display Card. If it is, conduct the 'Display_menu()' function below.
        if choice == 'Display Card':
            display_menu()
        # Check if the choice is Search Card. If it is, conduct the 'Search_menu()' function below.
        elif choice == 'Search Card':
            search_menu()
        # Check if the choice is Remove Card. If it is, conduct the 'Remove_menu()' function below.
        elif choice == 'Remove Card':
            remove_menu()
        # Check if the choice is Add Card Card. If it is, conduct the 'Add_menu()' function below.
        elif choice == 'Add Card':
            pass
        # Check if the choice is Edit Card. If it is, conduct the 'Modify_menu()' function below.
        elif choice == 'Edit Card':
            pass
        # Check if the choice is exiting the program. If it is, the program will print a message and suspend.
        elif choice == '[EXIT]':
            easygui.msgbox("Thanks for your visiting!", title = "GOOBYE")
            break

#Call the Main function here to make the whole program work.
main()
