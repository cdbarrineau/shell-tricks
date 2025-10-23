import time

count = 0
while True:
    print("\x1b[2K", end="")
    print("Count: " + str(count), end="\r")
    time.sleep(1)
    
    count = count + 1
