import random

def roll_dice(num_dice, num_rolls):
    for _ in range(num_rolls):
        results = [random.randint(1, 6) for _ in range(num_dice)]
        total = sum(results)
        print(f"Roll {_ + 1}: {results} (Total: {total})")

if __name__ == "__main__":
    try:
        num_dice = int(input("Enter the number of dice: "))
        num_rolls = int(input("Enter the number of rolls: "))
        
        if num_dice <= 0 or num_rolls <= 0:
            print("Please enter valid positive integers for the number of dice and rolls.")
        else:
            roll_dice(num_dice, num_rolls)
    
    except ValueError:
        print("Please enter valid integers for the number of dice and rolls.")
