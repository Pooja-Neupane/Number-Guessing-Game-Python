import random

def number_guessing_game():
    print("🎯 Welcome to the Number Guessing Game!")
    number_to_guess = random.randint(1, 100)
    attempts = 7

    for i in range(attempts):
        try:
            guess = int(input(f"\n🔢 Attempt {i+1}/{attempts}: Enter your guess (1-100): "))
            if guess < 1 or guess > 100:
                print("⚠️ Please enter a number between 1 and 100.")
                continue

            if guess == number_to_guess:
                print("🎉 Congratulations! You guessed the correct number!")
                break
            elif guess < number_to_guess:
                print("📉 Too low! Try again.")
            else:
                print("📈 Too high! Try again.")
        except ValueError:
            print("❌ Invalid input. Please enter a number.")
    else:
        print(f"\n😞 Sorry, you've used all your attempts. The number was {number_to_guess}.")

if __name__ == "__main__":
    number_guessing_game()
