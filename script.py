from stack import Stack

print("\nLet's play Towers of Hanoi!!")

#Create the Stacks
# where stacks will be stored
stacks = []
left_stack = Stack("Left")
middle_stack = Stack("Middle")
right_stack = Stack("Right")
stacks.append(left_stack)
stacks.append(middle_stack)
stacks.append(right_stack)



#SET UP GAME
num_disks = int(input("\nHow many disks do you want to play with? "))
# ensure num disks are at least 3
while num_disks < 3:
  num_disks = int(input("Enter number greater than 3, please!\n"))

# iterating from the highest backwards and pushing to left_stack
for i in range(num_disks, 0, -1):
  left_stack.push("Disk " + str(i))  

# For towers of hanoi, number of optimal moves is always 2 ** num_disks - 1
num_optimal_moves = 2 ** num_disks - 1
print("\nThe fastest you can solve this game is in {} moves.\n".format(num_optimal_moves))




#Get User Input
# helper function that prompts users to choose stack
def get_input():
  choices = [stack.get_name()[0] for stack in stacks]
  while True:
    for i in range(len(stacks)):
      name = stacks[i].get_name()
      letter = choices[i]
      print(f"Enter {letter} for {name}")
    
    user_input = input("").upper().strip()
    if user_input in choices:
      for i in range(len(stacks)):
        if user_input == choices[i]:
          return stacks[i]


        
#Play the Game
num_user_moves = 0
# game ends when right_stack is full
while right_stack.get_size() != num_disks:
  print("\n\n\n...Current Stacks...")
  for stack in stacks:
    print(stack.print_items())
  
  while True:
    print("\nWhich stack do you want to move from?")
    from_stack = get_input()
    print("\nWhich stack do you want to move to?")
    to_stack = get_input()
    # checking if user tried to move from empty stack
    if from_stack.is_empty():
      print("\n\nInvalid Move. Try again")

    # checking if stack moving to is empty
    # OR checking if stack moving from is smaller than stack moving to
    elif to_stack.is_empty() or from_stack.peek() < to_stack.peek():
      disk = from_stack.pop()
      to_stack.push(disk)
      num_user_moves += 1
      break
    # if user tries to move larger disk onto smaller disk
    else:
      print("\n\nInvalid Move. Try Again")

  print(f"\n\nYou completed the game in {num_user_moves} moves, and the optimal number of moves is {num_optimal_moves}")