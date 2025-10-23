import time

# print ("Doing Progress Bar...")

print("Processing...", end="\r")
time.sleep(2)
print("\x1b[2K", end="")
print("Done", end="\r")

# print("\x1b[2K", end="")
# print("Done!")