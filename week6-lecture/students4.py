import csv

name = input("Whats's your name? ")
home = input("WHere's your home? ")

with open("students4.csv", "a", newline='') as file:
    # In DictWriter, I have to specify the order ('fieldnames') in which those columns are when writing it out
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})