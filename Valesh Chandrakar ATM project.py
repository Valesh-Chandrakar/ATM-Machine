import time as t
user_pin = 1470
user_balance = 4578.50
user_name = "Mr. John"
print("Welcome to your bank account", user_name, end = "\n\n")


while (True):
    print("\t\t0. Logout and Exit")
    print("\t\t1. View Account Balance")
    print("\t\t2. Withdraw Cash")
    print("\t\t3. Deposit Cash")
    choice = int(input("Enter number to proceed > "))
    print("\n\n")


    if choice == 0:
        print("Exiting...")
        t.sleep(2)
        print("You have been logged out. Thank you!\n\n")
        break
    elif choice in (1, 2, 3):
        num_of_tries = 3
        while (num_of_tries != 0):
            input_pin = int(input("Please enter your 4-digit PIN > "))

            if input_pin == user_pin:
                print("Account auhtorized!\n\n")

                if choice == 1:
                    print("Loading Account Balance...")
                    t.sleep(2)
                    print("Your current balance is Rs.", user_balance, end="\n\n\n")
                    break

                elif choice == 2:
                    print("Opening Cash Withdrawal...")
                    t.sleep(1.5)

                    while (True):
                        withdraw_amt = float(input("Enter the amount you wish to withdraw > "))

                        if withdraw_amt > user_balance:
                            print("Can't withdraw Rs.", withdraw_amt)
                            print("low balance!")
                            continue

                        else:
                            print("Withdrawing Rs.", withdraw_amt)
                            confirm = input("Confirm? Y/N  ")
                            if confirm in ('Y', 'y'):
                                user_balance -= withdraw_amt
                                print("Amount withdrawn - Rs.", withdraw_amt)
                                print("Remaining balance - Rs.", user_balance, end="\n\n\n")
                                break

                            else:
                                print("Cancelling transaction...")
                                t.sleep(2)
                                print("Transaction Cancelled!\n\n")
                                break

                    break

                elif choice == 3:
                    print("Loading Cash Deposit...")
                    t.sleep(1.5)

                    deposit_amt = float(input("Enter the amount you wish to deposit > "))
                    print("Depositing Rs.", deposit_amt)
                    confirm = input("Confirm? Y/N > ")
                    if confirm in ('Y', 'y'):
                        user_balance += deposit_amt
                        print("Amount deposited - Rs.", deposit_amt)
                        print("Updated balance - Rs.", user_balance, end="\n\n\n")
                    else:
                        print("Cancelling transaction...")
                        t.sleep(1)
                        print("Transaction Cancelled!\n\n")

                    break


            else:
                num_of_tries -= 1
                print("PIN incorrect! Number of tries left -", num_of_tries, end="\n\n")

        else:
            print("Exiting...")
            t.sleep(2)
            print("You have been logged out. Thank you!\n\n")
            break


    else:
        print("Invalid input!")
        continue