#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random

print("==========================================")
print("       🎯 ULTIMATE GUESSING GAME")
print("==========================================")

print("\nSelect Difficulty Level:")
print("1. Easy   (10 Attempts)")
print("2. Medium (7 Attempts)")
print("3. Hard   (5 Attempts)")

choice = input("\nEnter your choice (1/2/3): ")

# Difficulty settings
if choice == "1":
    max_attempts = 10
    level = "Easy"

elif choice == "2":
    max_attempts = 7
    level = "Medium"

elif choice == "3":
    max_attempts = 5
    level = "Hard"

else:
    print("Invalid choice! Default difficulty set to Medium.")
    max_attempts = 7
    level = "Medium"

# Generate random number
secret_number = random.randint(1, 100)

print(f"\n🎮 Difficulty Level: {level}")
print("I have selected a number between 1 and 100.")
print(f"You have only {max_attempts} attempts!")
print("------------------------------------------")

# First clue
if secret_number % 2 == 0:
    print("🔍 Clue: The number is EVEN.")
else:
    print("🔍 Clue: The number is ODD.")

attempts = 0

# Game Loop
while attempts < max_attempts:

    try:
        guess = int(input(f"\nAttempt {attempts + 1}: Enter your guess: "))
        attempts += 1

        # Range validation
        if guess < 1 or guess > 100:
            print("⚠ Please enter a number between 1 and 100.")
            continue

        difference = abs(secret_number - guess)

        # Correct Guess
        if guess == secret_number:

            print("\n🎉 CONGRATULATIONS!")
            print(f"✅ You guessed the number {secret_number} correctly!")
            print(f"🏆 Attempts Used: {attempts}")

            # Performance
            if attempts <= 2:
                print("🌟 Outstanding Performance!")
            elif attempts <= 4:
                print("👏 Great Guessing Skills!")
            else:
                print("🙂 Nice Try! You made it!")

            break

        # High / Low hints
        elif guess > secret_number:
            print("📈 Too High!")

        else:
            print("📉 Too Low!")

        # Distance hints
        if difference <= 3:
            print("🔥 Extremely Close!")
        elif difference <= 7:
            print("😊 Very Close!")
        elif difference <= 15:
            print("🙂 Close!")
        else:
            print("🥶 Far Away!")

        # Remaining attempts
        remaining = max_attempts - attempts
        print(f"⏳ Remaining Attempts: {remaining}")

    except ValueError:
        print("❌ Invalid input! Please enter numbers only.")

# Lose condition
if guess != secret_number:
    print("\n💀 GAME OVER!")
    print(f"🎯 The correct number was: {secret_number}")
    print("Better luck next time!")


# In[ ]:




