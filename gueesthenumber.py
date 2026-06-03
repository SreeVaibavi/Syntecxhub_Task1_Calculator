import random

best_score = None

while True:
    print("\n=== NUMBER GUESSING GAME ===")
    print("1. Easy (1 - 10)")
    print("2. Medium (1 - 50)")
    print("3. Hard (1 - 100)")

    choice = input("Choose difficulty (1/2/3): ")

    if choice == "1":
        low, high = 1, 10
    elif choice == "2":
        low, high = 1, 50
    elif choice == "3":
        low, high = 1, 100
    else:
        print("Invalid choice!")
        continue

    number = random.randint(low, high)
    attempts = 0

    print(f"\nI have chosen a number between {low} and {high}.")

    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < number:
            print("Too low! Try a higher number.")
        elif guess > number:
            print("Too high! Try a lower number.")
        else:
            print(f"\n🎉 Correct! You guessed it in {attempts} attempts.")

            if best_score is None or attempts < best_score:
                best_score = attempts
                print(" New Best Score!")

            print("Best Score:", best_score)
            break

    play_again = input("\nPlay again? (yes/no): ").lower()

    if play_again != "yes":
        print("Thanks for playing!")
        print("Created by Sree Vaibavi V")
        break
