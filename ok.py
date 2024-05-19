while True:
    user_input = input("Enter an integer from 4 to 9, or 'quit' to exit: ")
    
    # Check if user wants to quit
    if user_input.lower() == 'quit':
        print("Exiting the program.")
        break
    
    # Check if user input is an integer
    try:
        user_input = int(user_input)
        if 4 <= user_input <= 9:
            print("Valid input:", user_input)
            # Do something with valid input
        else:
            print("Error: Please enter an integer between 4 and 9.")
    except ValueError:
        print("Error: Please enter an integer or 'quit'.")
while True:
    user_input = input("Enter an integer from 4 to 9, or 'quit' to exit: ")
    
    # Check if user wants to quit
    if user_input.lower() == 'quit':
        print("Exiting the program.")
        break
    
    # Check if user input is an integer
    try:
        user_input = int(user_input)
        if 4 <= user_input <= 9:
            print("Valid input:", user_input)
            # Do something with valid input
        else:
            print("Error: Please enter an integer between 4 and 9.")
    except ValueError:
        print("Error: Please enter an integer or 'quit'.")
