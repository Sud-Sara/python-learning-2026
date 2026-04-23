import csv

n = input("What's your name? ")
h = input("Where's your home? ")

with open("students.csv", "a", newline='') as file:
    writer=csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": n,"home":h})
