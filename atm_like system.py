dep_input = 0
print("Hello there! Welcome to Shield Bank.")
choice = int(input("Please choose an option:"))
print("1. Create an account")
print("2. Deposit")
print("3. Withdraw")
print("4. Check balance")
print("5. Exit")

created_acc = False

if choice == 1:
    print("Welcome to account creation.")
    name_entry = input("Please enter your name: ")
    print("Hello " + name_entry + ". Your account has been created successfully!")
    print("Your innitial account balance is 0, Thank you for choosing Shield Bank.")
    created_acc = True
    
elif choice == 2:
    if created_acc == False:
        print("You need to create an account first.")
    else:
        dep_input = int(input("Please enter the amount you want to deposit: "))
        print("You deposited " + dep_input + "$" + ". Thank you for using Shield Bank.")
    
    
elif choice == 3:
    if created_acc == False:
        print("You need to create an account first.")
    else:    
        with_input = int(input("Please enter the amount you want to withdraw: "))
        if with_input > dep_input:
            print("You cannot withdraw more than you have. Please try again.")
        else:
            print("You withdrew " + with_input + "$" + ". Thank you for using Shield Bank.")
            new_balance = dep_input - with_input
            print("Your new balance is " + new_balance + "$" + ". Thank you for using Shield Bank.")
        
elif choice == 4:
    if created_acc == False:
        print("You need to create an account first.")
    else:
        pin_input = int(input("Please enter your pin: "))
        if pin_input == 1234:
            print("Your balance is " + dep_input + "$" + ". Thank you for using Shield Bank.")
        else:
            print("Incorrect pin. Please try again.")
        
elif choice == 5:
    print("Thank you for using Shield Bank. Goodbye!")
