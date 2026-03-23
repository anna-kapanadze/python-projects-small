import random

doors = [1, 2, 3]
wins = 0
rounds = 0

print("Monty Hall Problem")
print("3 doors. 1 car. 2 goats.")
print("Pick a door, the host reveals a goat, then decide to switch or stay.\n")

while True:
    car = random.choice(doors)

    while True:
        try:
            pick = int(input("Pick a door (1, 2, 3): "))
            if pick in doors:
                break
            print("Enter 1, 2 or 3.")
        except ValueError:
            print("Enter a number.")

    host_options = [d for d in doors if d != pick and d != car]
    host_reveal = random.choice(host_options)
    print(f"Host opens door {host_reveal} - it's a goat!")

    choice = input("Switch doors? (y/n): ").strip().lower()
    switched = choice == "y"

    if switched:
        pick = [d for d in doors if d != pick and d != host_reveal][0]

    rounds += 1
    if pick == car:
        wins += 1
        print("You won the car!")
        if switched:
            print("You switched - and that's exactly why you won. Switching wins 2 out of 3 times.\n")
        else:
            print("You stayed - and got lucky this time. But staying only wins 1 out of 3 times.\n")
    else:
        print(f"Goat. The car was behind door {car}.")
        if switched:
            print("You switched but lost this time - it still happens 1 in 3 times.\n")
        else:
            print("You stayed. Switching would have won here - it does 2 out of 3 times.\n")

    print(f"Score: {wins}/{rounds}")

    again = input("Play again? (y/n): ").strip().lower()
    if again != "y":
        print(f"\nFinal: {wins} wins out of {rounds} games.")
        print("The main thing to remember here is that switching doors wins 67% of the time. The maths always wins.")
        break
