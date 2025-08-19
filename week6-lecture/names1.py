name = input("What's your name? ").strip().title()

# open() function alows to read from and write to a file
# It requires the name of the file that you want to open, and how you want to open it
# If the file doesn't exist, it will be created
# Opening on write mode ("w") recreates the file everytime you run the program
file = open("names1.txt", "a") 
file.write(f"{name}\n") # Add a name to it
file.close() # Close and save the file