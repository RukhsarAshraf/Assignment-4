import time

# input from user 
seconds = int(input("Enter time in seconds: "))

# countdown function
while seconds > 0:
    print(f"Time left: {seconds} seconds")
    time.sleep(1)  # wait for 1 second, sleep() function ka use hm timer mein delay dyne ke liye karengy.
    seconds -= 1
    
print("Time's up!")