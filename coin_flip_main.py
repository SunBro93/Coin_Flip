import time
import random

flip_counter = 0
heads_counter = 0
tails_counter = 0

def show_heads():
  print("""   
            *****
         *         *
        *   |   |   *
       *    |---|    *
        *   |   |   *
         *         *
            ***** """)

def show_tails():
  print("""
            *****
         * _______ *
        *     |     *
       *      |      *
        *     |     *
         *         *
            ***** """)
def waiting():
  print("\n.")
  time.sleep(0.5)
  print("..")
  time.sleep(0.5)
  print("...")
  time.sleep(0.5)

def flip():
  global heads_counter
  global tails_counter
  global flip_counter

  num = random.randint(1,6)
  if num % 2 == 0:
    waiting()
    show_tails()
    print("\nIt's Tails!")
    tails_counter += 1
    flip_counter += 1
  else:
    waiting()
    show_heads()
    print("\nIt's Heads!")
    heads_counter += 1
    flip_counter += 1

def show_stats():
  print("\nYou have made " + str(flip_counter) + " flips so far.")
  print("\nThere have been " + str(heads_counter) + " results of 'Heads'.")
  print("\nThere have been " + str(tails_counter) + " results of 'Tails'.")

def counter_reset():
  global flip_counter
  global heads_counter
  global tails_counter
  print("\nWould you like to reset the counters?")
  answer = input()
  if answer == "yes" or answer == "Yes" or answer == "y" or answer == "Y":
    flip_counter = 0
    heads_counter = 0
    tails_counter = 0
    print("\nYour counters have been reset!")
  else:
    print("\nYour counters have not been reset.")


def show_commands():
  print("""\n Commands:
  'flip' = Flip a coin and show the result.
  'stats' = Show the current stats for your coin flips.
  'reset' = Reset the current stats for your coin flips.
  'quit' = Exit the application.
  'help' = Shows a list of the available commands and an explanation of what each one does.""")


#Initialise the app
print("""______________________________________ """)
print("\nWelcome to 'PyFlip': Coin Flipping Simulator!")
print("\nUse key words to navigate the app:")
show_commands()

#main logic loop

while True:
  query = input("\nPlease enter a command. To view the list of available commands, enter 'help':\n")
  if query == "help" or query == "Help":
    show_commands()
  elif query == "flip" or query == "Flip":
    flip()
  elif query == "stats" or query == "Stats":
    show_stats()
  elif query == "reset" or query == "Reset":
    counter_reset()
  elif query == "quit" or query == "Quit":
    quitting = input("\nAre you sure you want to quit?\n")
    if quitting == "yes" or quitting == "Yes" or quitting == "y":
      print("\nThanks for using PyFlip by SunBroSoft. Bye!")
      break
    else:
      pass
  else:
    print("\nThis command is invalid.")
