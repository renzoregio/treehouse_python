
def main():
    TICKET_PRICE = 10
    tickets_remaining = 100
    
    try:
        while tickets_remaining:
            # output how many tickets are remaining using the tickets_remaining variable
            print("There are {} tickets remaining!".format(tickets_remaining))
            # gather the user's name and assign it to a new variable
            name = str(input("What is your name?    "))
            # prompt the user by name and ask how many tickets they would like
            num_tickets = int(input("Hi, {}! How many tickets would you like?   ".format(name)))
            if num_tickets > tickets_remaining:
                raise ValueError("We only have {} tickets in our inventory... Try again!".format(tickets_remaining))
            # calculate the price (number of tickets multiplied by the price) and assign it to a variable
            amount_due = num_tickets * TICKET_PRICE
            # output the price to the screen
            print("For {} tickets, it will be ${}".format(num_tickets, amount_due))
            # prompt user if they want to proceed
            print("Would you want to continue to your purchase? If yes, please enter 'YES'. If not, enter 'NO'.")
            proceed =  input("")
            # if user wants to proceed
            if proceed.lower() == "yes":
                print("SOLD! {}, you just purchased {} tickets for ${}. Enjoy!".format(name, num_tickets, amount_due))
                # subtracts the total tickets remaining with the tickets purchased by the user
                tickets_remaining -= num_tickets
            # if user does not want to proceed
            elif proceed.lower() == "no":
                print("Thank you anyway, {}! If you reconsider, we'll be here!".format(name))
            else:
                pass
                # do something
        if tickets_remaining == 0:
            print("We are SOLD OUT!")
    except ValueError as err:
        print("({})".format(err))

if __name__ == "__main__":
    main()