def bool_ans(prompt):
    """
    Handles yes/no input.
    """
    while True:
        response = input(prompt + " [y/n]\n").lower()
        if response == 'y':
            return True
        elif response == 'n':
            return False
        print("Please enter either 'y' or 'n'.")


def num_ans(prompt):
    """
    Handles numerical input.
    """
    while True:
        response = input(prompt + "\n")
        try:
            return int(response)
        except ValueError:
            print("Please enter a numeric value.")
