Balance  = 100000
Pin = 1234

print("=====WELCOME TO ATM=====")
attempts = 3
while attempts > 0:

    entered_pin = int(input("Enter Your Pin:"))

    if entered_pin == Pin:
        while True:
            print("ATM MENU")
            print("1. check balance")
            print("2. withdraw money")
            print("3. deposit money")
            print("4. exit")
    
    
        
            choice = int(input("enter your choice:"))

            if choice == 1:
                    print("Your Account Balance Is Rs",Balance)
    
            elif choice == 2:
                        amount = int(input("Enter amount to withdraw: Rs"))

                        if amount <= Balance:
                            Balance = Balance - amount
                            print("Your remaining balance is: Rs", Balance)
                        else:
                            print("Insufficient Balance")
        
            elif choice == 3:
                    amount = int(input("Enter amount: Rs"))
                    Balance = amount + Balance
                    print("Your amount deposited successfully")
                    print("Your new balance is: Rs", Balance)
    
            elif choice == 4:
                print("Thank You For Using The ATM!")
                break

            else:
                print("invalid choice")

        break
    
    else:
        attempts = attempts - 1

        if attempts > 0:
            print("wrong pin!")
            print("attempts remaining:", attempts)
        else:
            print("No attempts left!/n Your account is locked.")
        
            
       
    
    
    
      
