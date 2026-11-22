import os

# Specify the directory path
path = "."

# Get all files and folders inside the directory
items = os.listdir(path)

# Print all items
print("Files and Folders:")

for item in items:
    print(item)