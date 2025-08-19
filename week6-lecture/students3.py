import csv

name = input("Whats's your name? ")
home = input("WHere's your home? ")

with open("students3.csv", "a", newline='') as file:
    writer = csv.writer(file)
    writer.writerow([name, home])