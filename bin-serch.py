import math
import time

# ASCII art featuring the two bunny predictors
AI_ART = """
 ∧_∧   ∧_∧
( ◍’꒳’ ))`ᵕ’◍) ~♡  < [AI Predictors]
/     づ⊂    ヽ
"""

def binary_search(count, target):
    low = 1
    high = count
    while low <= high:
        print("\n[We are calculating the next step...]")
        time.sleep(1.2)
        
        mid = (low + high) // 2
        guess = mid
        
        if guess == target:  # If guess is correct
            print(f"\n[+] We found it! Your number is: {guess} (index = {mid - 1})")
            return mid
            
        elif guess < target:  # If guess is too low
            print(f"Our guess is {guess}, right? [y/n]")
            answer = input("> ").lower()
            if answer == 'y':
                print("No, we feel you are deceiving us. You have made a different number, we are looking further.")
                time.sleep(1)
                low = mid + 1
            elif answer == 'n':
                print(f"Oh, your number is higher than our guess. We thought it was {guess}.")
                low = mid + 1
            else:
                print("Invalid input. Assuming your number is higher than our guess.")
                low = mid + 1 
                
        else:  # If guess was higher than target
            print(f"Our guess is {guess}, right? [y/n]")
            answer = input("> ").lower()
            if answer == 'y':
                print("No, we feel you are deceiving us. You have made a different number, we are looking further.")
                time.sleep(1)
                high = mid - 1
            elif answer == 'n':
                print(f"Oh, your number is lower than our guess. We thought it was {guess}.")
                high = mid - 1
            else:
                print("Invalid input. Assuming your number is lower than our guess.")
                high = mid - 1
            
    print("Number not found")
    return None

# --- Program start ---
print(AI_ART)
time.sleep(0.5)
print("Hi! Enter count of numbers (max count 1000000000 numbers):")

try:
    count = int(input("> "))
    if count < 1 or count > 1000000000:
        print("Your count of numbers cannot be more than 1000000000 and less than 1.")
    else:
        print(f"Enter a number (1-{count}), and we will guess it.")
        try:
            number = int(input("> "))
            if number < 1 or number > count:
                print(f"Please enter a number between 1 and {count}.")
            else:
                attempts = math.ceil(math.log2(count))
                
                print("\nWe are analyzing the parameters...")
                time.sleep(1.5)
                print(f"[AI]: Easy! We will guess your number in {attempts} attempts at most.")
                time.sleep(1.5)
                
                print("Starting binary search...")
                time.sleep(1)
                
                binary_search(count, number)
                
        except ValueError:
            print("Invalid input. Please enter a valid number.")
except ValueError:
    print("Invalid input. Please enter a valid number.")