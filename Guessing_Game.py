import random

wallet = {1: 100}


def num():
    """Return a random number"""
    rand_num = random.randint(1, 3)
    return rand_num


def guess():
    """Evaluate the players guess."""
    print("I see you have ${}".format(wallet[1]))
    ante = eval(input("How many dollars would you like to bet(10/50/100): "))

    if ante != 100 and ante != 50 and ante != 10:
        print("That is not a valid answer...")
        print("Please try again...")
        guess()

    elif ante > wallet[1]:
        print("You are betting more than you have...")
        print("Please try again...")
        guess()

    else:
        print("You bet ${}".format(ante))
        player_num = eval(input("Guess a number, your choices are 1/2/3: "))

        if player_num >= 4 or player_num == 0:
            print("Please try again...")
            guess()

        elif player_num == num():
            after_win = int(wallet[1]) + ante
            wallet.update({1: after_win})
            print("You win!")
            print("You now have ${}".format(after_win))
            # print(after_win)
            restart()

        else:
            print("Wrong!")
            wrong = int(wallet[1]) - ante

            if wrong <= 0:
                print("You are out of funds :(")
                end_game()

            else:
                wallet.update({1: wrong})
                print("You now have ${}".format(wrong))
                restart()


def restart():
    """Restart the game."""
    again = input("Would you like to play again(y/n)?: ")
    if again != "y" and again != "n":
        print("That is not a valid answer...")
        restart()

    elif again == "y":
        print("*********************************")
        main()

    else:
        end_game()


def end_game():
    end = ["Thanks for playing!",
           "Have a good day!"]
    return print(random.choice(end))


def main():
    """Run the main block of code."""
    hello = ["Welcome to the table...",
             "Let's play!"]
    print(random.choice(hello))
    num()
    print("The house has selected it's number...")
    guess()


main()