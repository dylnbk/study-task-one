# study-task-one
Some basic python exercises

# instructions
*Combine each of the the tasks into one python file*

**Task 1 - Input and Reverse**
1. The user will be prompted to enter a word. 
2. When the user presses enter, the word is added to a list of words. 
3. This continues until the user enters the word ‘quit’.  
4. If the user enters ‘quit’, each of the words previously entered are printed in reverse.
5. This is followed by a line that tells the user how many words they entered. 
6. The program should not exit until the word ‘quit’ is entered.
7. The word ‘quit’ should not be added to the list.

**Task 2 – Guessing game**
1.	The program will create a random number between 1 and 25. 
2.	The user will be prompted to guess the number. 
3.	Every guess will be added to a list of guesses.
4.	After every guess, the user will see, in one row, all the guesses they have made and, if the user is incorrect, a prompt to try again. 
5.	If the guess is correct, the user will see a list of guesses in one row, the number of guesses they took in another row, the correctly guessed number in a third row. 
6.	The game will not end until the correct number is guessed.

**Task 3 – Shopping list**
1.	When the program starts, the user will be prompted to enter ‘a’ to add items to their shopping list or enter ‘q’ to quit.
2.	After adding an item, the user will see it listed in the menu with a number beside it and an additional menu prompt allowing them to select an item. 
3.	The item number should be one more than the index in the list where the item is added.
4.	The user will be able to select the item using the number. 
5.	If the user selects an item, they are prompted for the price they paid. 
6.	Upon entering the price, the item will re-appear in the list with the price paid and a note ‘purchased’ beside it. 
7.	If the user selects a purchased item, a message will be displayed telling them the item was already purchased.
8.	The program will always display the main menu after every entry until the user enters q to quit. 

**Task 4 – Product stock list**
1.	When the program starts, the user will see a menu with the options ‘view products’, ‘add product’, ‘quit’.
2.	If the user selects the option ‘add product’, they will be prompted to add a products title, price, location and qty in stock. 
3.	After adding these details, the product will be displayed and the menu shown again. 
4.	If the price is less than £1.00, it will be displayed in pence, otherwise it will be displayed in pounds and pence. 
5.	If a user selects ‘view products’, all the products that were added will be displayed. Each product is displayed on a single row, separated by a dash.
6.	If a user selects quit, the program quits. 
7.	The program will show the menu after each entry until the user selects the option to quit. 

**Task 5 – Seminar**
1.	The program will start with a main menu. The options are: 
      - Add attendee
      - Remove Attendee
      - Confirm Attendance
      - List Attendees
      - Quit program
      
2.	On selecting 1, ‘Add attendee’, the user is prompted for the attendees’ name and month and year of birth. 
3.	This will be added to a list of attendees. 
4.	On selecting 2, ‘Remove attendee’, the user is prompted for the attendees’ name. If the name is found in the list, the attendee will be removed, and user notified. If the attendee is not in the list, the user will see an error that the attendee is not in the list. 
5.  On selecting 3. ‘Confirm attendance’, the attendees will be listed. 
      - The user will be prompted to select the attendee to confirm attendance, or to press ‘#’ to return to the main menu. 
      - If a user enters an index matching an attendee in the list, that person will be marked as attended. 
      - If a user enters #, they will see the main menu again. 
      
6.	If the user selects 4, ‘List attendees’, they will see a list of attendee names, month and year of birth and confirmation of attendance
7.	If the user selects 5 to quit, the program will end. 
8.	The program will otherwise show the main menu again after every entry is completed.
