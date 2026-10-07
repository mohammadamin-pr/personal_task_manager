from dotenv import load_dotenv
import os

from tasks import add_task, show_tasks, save_tasks

load_dotenv()

name = input("What is your name: ")

print(f"Welcome, {name}")

admin = input("Do you want to enter Admin Mode? ")

if admin == "yes":
    password = input("Enter admin password: ")

    if password == os.getenv("TASK_MANAGER_ADMIN_PASSWORD"):
        print("Admin Mode")
    else:
        print("Wrong password")

tasks = []

while True:
    task = input("Enter a task (or type end to finish): ")

    if task == "end":
        break

    add_task(tasks, task)

save_tasks(tasks)
show_tasks(tasks)