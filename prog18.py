pin = 2008
balance = 12000
p = int(input("Enter the PIN: "))
if p == pin:
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print("Balance: ", balance)
    elif choice == 2:
        amount = int(input("Enter deposit amount: "))
        Balance = balance + amount
        print("New Balance: ", Balance)
    elif choice == 3:
        amount = int(input("Enter withdrawal amount: "))
        balance = balance - amount
        print("New Balance: ", balance)
    else:
        print("Invalid choice")
      
else: print("Wrong PIN")
