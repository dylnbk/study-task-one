#Task 1 - Input and Reverse

def stuff():
    words = []
    print()
    while True:
        check = input("Please enter a word, to end program type 'quit': \n")
        if check != "quit":
            words.append(check)
        else:
            words.reverse()
            print()
            for x in range(len(words)):
                print(words[x])
            print(f"\nThere are {len(words)} words in the list\n")
            break

#Task 2 – Guessing game

import random

def game():
    num = random.randint(1,25)
    guess = []
    attempts = 0
    print()
    while True:
        attempts += 1
        user_num = int(input("Guess a number between 1 and 25: \n"))
        guess.append(user_num)
        if user_num == num:
            print("You guessed",', '.join([f"{x}" for x in guess]))
            print(f"You took {attempts} guesses")
            print(f"The correct number is {num}\n")
            break
        else:
            print("You guessed",', '.join([f"{x}" for x in guess]))
            print("Please try again")
            continue

#Task 3 – Shopping list

def shop():

    shopping = {}
    key = 0
    choice = input("\na. Add an item\nq. Quit program\n\n")
    
    while True:
        
        if choice == "a":
            item = input("\nWhat would you like to add?\n\n")
            key += 1
            shopping.update({key:item})
            for x, y in shopping.items():
                print(f"\n{x}. {y}", end = ' ')
            choice = input("\n\na. Add an item\nq. Quit program\nor select an item:\n\n")

        elif choice.isdigit() == True:
            value = int(choice)
            if value in shopping:
                if "Purchased" in shopping[value]:
                    print("\nThis item was already purchased\n")
                    choice = input("\na. Add an item\nq. Quit program\nor select an item:\n\n")
                else:
                    price = float(input("\nHow much did you pay?\n\n"))
                    price = "£" + "{:.2f}".format(price)
                    shopping[value] += f": {price} - Purchased" 
                    for x, y in shopping.items():
                        print(f"\n{x}. {y}", end = ' ')
                    choice = input("\n\na. Add an item\nq. Quit program\nor select an item:\n\n")

        else:
            print("\nEnd program")
            break

#Task 4 – Product stock list

def main():

    key = 0
    products = {}
    
    while True:
        
        choice = input("\nPlease enter:\n'a' to add product\n'v' to view products\n'q' to quit\n")
        
        if choice.lower() == "a":
            key += 1
            item_name = input("\nWhat would you like to add?\n")
            price = float(input("What is the price?\n"))
            location = "Aisle " + input("Which number aisle is it located?\n")
            quantity = input("How much is available in stock?\n") + " in stock"
            
            if price < 1:
                price = "{:.2f}".format(price) + "p"
                products_item = {"name": item_name.capitalize(), "price": price, "location": location, "stock": quantity}
                products[key] = products_item

            else:
                price = "£" + "{:.2f}".format(price)
                products_item = {"name": item_name.capitalize(), "price": price, "location": location, "stock": quantity}
                products[key] = products_item
            print()
            print(" - ".join([x for x in products_item.values()]))

        elif choice.lower() == "v":
            print()
            for x, y in products.items():
                print(" - ".join([w for w in y.values()]))
                
        else:
            break

#Task 5 – Seminar Attendance

def register():

    attendee = {}
    key = 0

    while True:

        choice = int(input("\n1. Add Attendee\n2. Remove Attendee\n3. Confirm Attendance\n4. List Attendees\n5. Quit Program\n"))

        if choice == 1:
            key += 1
            info = input("\nPlease input the name, month and year of birth for the attendee:\n")
            attendee[key] = info.title()

        elif choice == 2:
            stop = False
            remove = input("\nPlease input the name of the attendee you wish to remove:\n")
            for x, y in dict(attendee).items():
                if remove.capitalize() in y:
                    print(f"\n{remove.capitalize()} has been removed from the list\n")
                    del attendee[x]
                    stop = True
                    break
            if not stop:
                print(f"\n{remove.capitalize()} is not on the list of attendees")

        elif choice == 3:
            stop = False
            print("\n".join([x for x in attendee.values()]))
            selection = input("\nPlease input the name of the attendee you wish to confirm attendance, or type '#' to return to the main menu:\n")
            if selection == "#":
                pass
            else:
                for x, y in dict(attendee).items():
                    if selection.capitalize() in y:
                        attendee[x] += ": Attendance Confirmed"
                        stop = True
                        break
                if not stop:
                    print(f"\n{selection.capitalize()} is not on the list of attendees")
                    

        elif choice == 4:
            print()
            print("\n".join([x for x in attendee.values()]))

        else:
            print("\nProgram closed")
            break

#Run the tasks :)

def run():

    while True:
        
        print("- - - - - - - -")
        
        go = int(input("\nWhich task do you wish to run?\n\n1. Input and Reverse\n2. Guessing game\n\
                       3. Shopping list\n4. Product stock list\n5. Seminar Attendance\n6. Quit program\n\n"))

        if go == 1:
            stuff()
        elif go == 2:
            game()
        elif go == 3:
            shop()
        elif go == 4:
            main()
        elif go == 5:
            register()
        elif go == 6:
            print("\nEnd program")
            break
        else:
            print("\nPlease enter a valid selection\n")

run()
