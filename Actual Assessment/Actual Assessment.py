
'''
Essential introdution: When the users use this program, an interface will show up with six different buttons for them to utilise.
The buttons are 'Display Card', 'Search Card', 'Remove Card', 'Add Card', 'Edit Card' & 'Exiting the program'.



'''









# Import the Easygui module
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
    
    # This is the place where the information (eg., card names and their values) will be stored in. In other words, save it into a variable.
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







# [THE CODE BELOW ALLOWS THE USERS TO ADD THEIR OWN ABILITIES INSTEAD OF THE GIVEN ABILITIES (eg., Strength, Speed, Stealth & Cunning), WHICH ISN'T WHAT WE WANT; WE WANT THE USER TO ONLY ENTER THE VALUES FOR EACH OF THE GIVEN ABILITIES.]
# [IN A NUTSHELL, THIS CODE IS DYNAMIC ESPECIALLY WHEN THE USERS WANT TO TYPE DOWN THEIR OWN ABILITIES AND VALUES.]


# ----------------------------------------------------------------------------------------------------------

# def add_menu():
#     add_card = easygui.enterbox("Enter the card's name: ", title = "ADD PAGE")

#     if not add_card:
#         easygui.msgbox("Your input cannot be blank; please try again.", title = "NOTE")
#         return

#     if add_card in cards:
#         easygui.msgbox(f"{add_card} is already exists; please try something else.", title = "NOTE")
#         return
    
#     card[add_card] = {}

#     for i in range(4):
#         while True:
#             abilities = easygui.enterbox("Enter an ability: ", title = "ADD PAGE")
#             if not abilities:
#                 easygui.msgbox("The ability column cannot be empty.", title = "NOTE")
#             else:
#                 break
        
#         while True:
#             try:
#                 values = easygui.enterbox(f"Enter the value (1-25): ", title = "ADD PAGE")
#                 if not values:
#                     easygui.msgbox("The value column cannot be empty.", title = "NOTE")
#                 else:
#                     values = int(values)
#                     break
#             except ValueError:
#                 easygui.msgbox("Invalid value; please try to enter a number from 1 to 25.")
        
#         cards[add_card][abilities.title()] = values
    
#     easygui.msgbox(f"{add_card} has been successfully added!", title = "SUCCESS")

# ----------------------------------------------------------------------------------------------------------




# [I HAVE CHANGED TO A DIFFERENT VERSION THAT ALIGNS WITH THE REQUIREMENT]
# [THE CODE BELOW IS A FIXED VERSION FROM THE CODE ABOVE THAT ONLY ALLOWS THE USERS TO ENTER THE VALUES FOR EACH ABILITY]:



# This is function where the users can add their own values for their given abilities.
def add_menu():
    add_card = easygui.enterbox("Enter the card's name:", title = "ADD CARD")

    add_card = add_card.title()

    # If the users don't type anything down, a text will inform them and return to the main menu, which is the Main function.
    if not add_card:
        easygui.msgbox("Your input cannot be empty; please try to enter a card's name.", title = "NOTE")
        return
    
    # If user's entered card is already exists in the card list, a message will inform them to type down a different card name.
    if add_card in cards:
        easygui.msgbox(f"Card '{add_card}' is already exists; please try to enter a different name for your card.", title = "NOTE")
        return
    

    # Below are four while loops (four different abilities) to check the valiadity for user's entered values. If not, the program will tell them to try again.
    while True:
        try:
            strength = int(easygui.enterbox(f"Enter the strength for {add_card} (1-25): "))
            if strength < 1 or strength > 25:
                easygui.msgbox(f"Your strength value must be between 1-25. Currently, your value is {strength}.")
            else:
                break
        except ValueError:
            easygui.msgbox("Please enter a valid number from 1-25.")

    while True:
        try:
            speed = int(easygui.enterbox(f"Enter the speed for {add_card} (1-25): "))
            if speed < 1 or speed > 25:
                easygui.msgbox(f"Your strength value must be between 1-25. Currentlyss, your value is {speed}.")
            else:
                break
        except ValueError:
            easygui.msgbox("Please enter a valid number from 1-25.")

    while True:
        try:
            stealth = int(easygui.enterbox(f"Enter the stealth for {add_card} (1-25): "))
            if stealth < 1 or stealth > 25:
                easygui.msgbox(f"Your stealth value must be between 1-25. Currently, your value is {stealth}.")
            else:
                break
        except ValueError:
            easygui.msgbox("Please enter a valid number from 1-25.")

    while True:
        try:
            cunning = int(easygui.enterbox(f"Enter the cunning for {add_card} (1-25) : "))
            if cunning < 1 or cunning > 25:
                easygui.msgbox(f"Your cunning value must be between 1-25. Currently, your value is {cunning}.")
            else:
                break
        except ValueError:
            easygui.msgbox("Please enter a valid number from 1-25.")

    # After the users have entered the correct values for the four abilities, they will be recorded correspondingly into their dictionary.
    cards[add_card] = {
        'Strength': strength,
        'Speed': speed,
        'Stealth': stealth,
        'Cunning': cunning
    }

    # This is a final message to inform the users that their card has been added successfully. 
    easygui.msgbox(f"Your card '{add_card}' has been successfully added!\n\nIf you would like to modify/edit anything for your card, head to the 'Edit Card' button.", title = "SUCCESS")

# This is the function for the users to modify any details in their card if they unintentionally typed a wrong information.
def modify_card():
    if not card:
        easygui.msgbox("Sorry, there is no card available to modify.", title="NOTE")
        return
    
    name = easygui.buttonbox("Choose a card to modify:", title="MODIFY CARD", choices=list(card.keys()))
    if not name:
        return
    
    current = card[name]
    
    msg = f"Current stats for {name}:\n"
    for stat, value in current.items():
        msg += f"{stat}: {value}\n"
    msg += "\nSelect which stat to modify:"
    

    change = easygui.buttonbox(msg, title = "MODIFY STAT", choices = list(current.keys()) + ["Cancel"])
    if change == "Cancel":
        return
    
    new_value = easygui.integerbox(f"Enter new value for {change} (1-25):", title = "NEW VALUE", min = 1, max = 25)
    if new_value is None:
        return
    
    card[name][change] = new_value
    easygui.msgbox(f"{name}'s {change} has been updated to {new_value}", title = "SUCCESS")



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
            add_menu()
        # Check if the choice is Edit Card. If it is, conduct the 'Modify_menu()' function below.
        elif choice == 'Edit Card':
            pass
        # Check if the choice is exiting the program. If it is, the program will print a message and suspend.
        elif choice == '[EXIT]':
            easygui.msgbox("You have exited the program", title = "GOOBYE")
            break

#Call the Main function here to make the whole program work.
main()
