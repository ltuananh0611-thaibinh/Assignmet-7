time_spent = input("Enter time spent (hours): ")

with open("time_spent.txt", "w") as file:
    file.write(time_spent)
    