# Personal Task Manager
A simple task manager built with Python for learning git - github
![Static Badge](https://img.shields.io/badge/python-blue?logo=python&logoColor=white)


## Features
- add multiple tasks
- save tasks
- load saved tasks
- admin mode
- set task priority

## Task priority
each task can have one of these priority levels:
- low
- medium 
- high

## Requirements
- Python
- python-dotenv

## Project Structure
```text
personal_task_manager2/
│   .env.example
│   .gitignore
│   main.py
│   README.md
│   requirements.txt
│   tasks.py
│
│
├───gif/
│       demo.mp4
│
├───images/
│       screenshot1.png
```

## Installation
Install pip the required packages:

```bash
python -m pip install -r requirements.txt
```

## Envoirment Setup
create a `.env` file in the project folder

Use `.env.example` as a template

Add your admin password

```env
admin_pass=your_password_here
```
replace `your_password here` with your own admin password

## Run the Program
run the main file:
```bash
python main.py
```

## Screenshot
![run project](C:\Users\Vahedi\Desktop\personal_task_manager2\images\screenshot.png)

## Demo
![demo](C:\Users\Vahedi\Desktop\personal_task_manager2\gif\demo.gif)
