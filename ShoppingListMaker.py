# Objective:
# The aim of this assignment is to create a program that helps users make a shopping list.

# Task 1: Write a function that lets the user add items to a list.
# Task 2: Include a feature to remove items from the list.
# Task 3: Add a function that prints out the entire list in a formatted way.



items = []


def shoppingList():
    while True:
        print("Shopping List for the week\n")
        
        print("[View] list")
        print("[Add] items to list")
        print("[Remove] items from list")
        print("[Exit]")
        pick = input("Which would you like to do?")

        
        if pick.lower() == "add":
            new = input("What would you like to add to the list?")
            items.append(new)
            print(f"{new} was added to the list")
            
        elif pick.lower() == "remove":
            removeItem = input("What item would you like to Remove?")
            if removeItem in items:
                items.remove(removeItem)
                print(f"{removeItem} was removed from list.")
            else:
                print(f"{removeItem} was not in the list!")

        elif pick.lower() =="view":
            print("Shopping List: ")
            print(items)
            
                
        elif pick.lower() == "exit":
            print("Goodbye!")
            break        

shoppingList()