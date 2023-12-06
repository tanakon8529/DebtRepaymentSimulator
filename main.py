# Define the initial debt data
debts = {'o1': 1, 'o2': 2, 'o3': 3, 'o4': 4, 'o5': 10, 'o6': 2, 'o7': 7}

# Initialize a variable to keep track of the current month
current_month = 1

# Calculate the total debt
total_debt = sum(debts.values())

# Calculate the monthly payment
monthly_payment = total_debt / 6

# Print the table header
print("Month\tDebtor\tPay\tPayment\tRemaining Debt")

# Run the debt payment process for 6 months
while current_month <= 6:
    # Initialize the remaining payment for this month
    remaining_payment = monthly_payment
    
    # Print the payments for each debtor this month
    for debtor, amount in debts.items():
        if amount == 0:
            continue  # Skip debtors with no remaining debt
        
        # Calculate the payment for this debtor this month
        payment = min(remaining_payment, amount)
        
        # Update the debt for the debtor
        debts[debtor] -= payment

        # Print the payment and remaining debt for this debtor
        print(f"{current_month}\t{debtor}\t{payment:.2f}\t{remaining_payment:.2f}\t{debts[debtor]:.2f}")
        
        # Deduct the payment from the remaining payment for this month
        remaining_payment -= payment
    
    # Add a line separator between payment months
    print("-" * 40)
    
    # Move to the next month
    current_month += 1
