import random
from re import S

print("Welcome to Rock Paper Scissors!")

computer = ["R", "P", "S"]
 
while True:
     user_choice = input("Enter a choice (R,P,S): ").upper()
     if user_choice in computer:
         computer_choice = random.choice(computer)
         print(f"\nPlayer {user_choice}, computer {computer_choice}.\n")
         
         
 
         if user_choice == computer_choice:
             print("It's a tie!")
         elif user_choice == "R":
             if computer_choice == "S":
                 print("Player wins")
                 
             else:
                 print("Computer wins")
                 
                 
         elif user_choice == "P":
             if computer_choice == "R":
                 print("Player wins")
                 
             else:
                 print("Computer wins")
                 
                 
         elif user_choice == "S":
             if computer_choice == "P":
                 print("Player wins")
                 
             else:
                 print("Computer wins")
                 
                 
                 
     else:
         print("Error, try again.")

         play_again = input("Play again? (yes/no): ").lower()

         if play_again != "yes":
                  break
print("Bye!")
