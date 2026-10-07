name = input("What is your name: ")
print(f"Welcome, {name}")

tasks = []

while True:
    task = input("Enter a task (or type end to finish): ")

    if task == "end":
        break

    tasks.append(task)

print("Your tasks:")

for task in tasks:
    print(task)