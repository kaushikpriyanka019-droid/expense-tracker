# Variable to store total expenses
total = 0

# Infinite loop
while True:

    # Ask user to enter expense
    expense = input("Enter expense amount (or type 'quit' to stop): ")

    # Check if user wants to stop
    if expense == "quit":
        break

    # Convert text into number
    expense = int(expense)

    # Add expense to total
    total = total + expense

# Display final result
print("Total Spent =", total)
