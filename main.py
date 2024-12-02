MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1


def deposit():
    while True:
        amount = input("Please enter the amount you'd like to deposit. $: ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than $0")
        else:
            print("Please enter a number.")

    return amount


def get_number_of_lines():
    while True:
        lines = input(
            "Please enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            # good way to check if a value is in-between another
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Number must be greater than 0.")
        else:
            print("Please enter a number.")

    return lines


def get_bet():
    while True:
        amount = input(
            "Please enter the amount you'd like to bet on each line. $: ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}")
        else:
            print("Please enter an amount.")

    return amount


def main():
    balance = deposit()
    lines = get_number_of_lines()
    print(balance, lines)


main()
