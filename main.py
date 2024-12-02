MAX_LINES = 3


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


def main():
    balance = deposit()


main()
