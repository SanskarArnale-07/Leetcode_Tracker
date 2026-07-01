import json
import os
DATA_FILE = os.path.join(os.path.dirname(__file__),"data.json")
print("Main.py Location", os.path.dirname(os.path.abspath(__file__)))
problems = []
def add_problem(problems):
#Storing all this in dictionary and dictionaries into list
    problem_name=input("Enter the Name of the Problem: ")
    difficulty= get_difficulty()
    topic= input("Enter the Topic of the Problem: ")
    date = input("Enter the Date you Solved the Problem: ")
    problem_overview = {"problem_name" : problem_name, "difficulty": difficulty, "topic":topic, "date":date}
    print(problem_overview)
    problems.append(problem_overview)
def get_difficulty():
    while True:
        difficulty = input("Enter the Difficulty of the Problem: ")
        difficulty = difficulty.lower()
        if difficulty in ["easy", "medium", "hard"]:
            return difficulty
        print("Invalid Difficulty. Please Enter Easy, Medium or Hard.")
def view_problems(problems):
    for index , problem in enumerate(problems,start=1):
        print(index)
        print(problem)
def save_data(problems , filename):
    with open(filename, "w") as f:
        json.dump(problems,f)
def load_data():
    try:
        with open(DATA_FILE, "r") as f:
            problems = json.load(f)
            return problems
    except FileNotFoundError:
        print("No previous data found\nStarting with an empty list")
        return []
def search_problems(problems):
    try:
        choice = int(input("Enter your choice:\n1)Problem Name\n2)Difficulty\n3)Topic"))
        if choice == 1:
            problem_name = input("Enter the Name of the Problem: ")
            found = False
            for problem in problems:   #problems is a list and problem is a dictionary
                if problem["problem_name"] == problem_name:    
                    found = True
                    print_problem(problem)
            if not found:
                print("No Problem found")
        elif choice == 2:
            difficulty_name=input("Enter the Difficulty of the Topic: ")
            found = False
            for problem in problems:   #problems is a list and problem is a dictionary
                if problem["difficulty"] == difficulty_name:    
                    found = True
                    print_problem(problem)
            if not found:
                print("No Problem found")
        elif choice == 3:
            topic_name=input("Enter the Name of the Topic: ")
            found = False
            for problem in problems:   #problems is a list and problem is a dictionary
                if problem["topic"] == topic_name:    
                    found = True
                    print_problem(problem)
            if not found:
                print("No Problem found")
    except ValueError:
        print("Enter specified choice numbers: ")
def print_problem(problem):
    print("Problem Name:",problem["problem_name"],"\nDifficulty: ", problem["difficulty"], "\nTopic: ", problem["topic"], "\nDate: ", problem["date"])   
def delete_problem(problems):
    problem_name = input("Enter the Name of the Problem: ")
    found = False
    for problem in problems:
        if problem_name == problem["problem_name"]:
            problems.remove(problem)    #From the Problems list remove the xyz problem dictionary
            print("Problem Has been Deleted")
            found = True
            save_data(problems, DATA_FILE)
            break
    if not found:
        print("Problem Does not Exist")
def edit_problem(problems):
    problem_name = input("Enter the Name of the Problem: ")
    found = False
    for problem in problems:
        if problem_name == problem["problem_name"]:
            found = True
            choice = int(input("Enter your choice:\n1)Name:\n2)Difficulty\n3)Topic\n4)Date"))
            if choice == 1:
                name = input("Enter the Updated Name of the Problem: ")
                problem["problem_name"] = name
            elif choice == 2:
                difficulty = input("Enter the Updated Difficulty of the Problem: ")
                problem["difficulty"] = difficulty
            elif choice == 3:
                topic = input("Enter the Updated Topic of the Problem: ")
                problem["topic"] = topic
            elif choice == 4:
                date = input("Enter the Updated Date of the Problem: ")
                problem["date"] = date
            save_data(problems, DATA_FILE)
            print("Problem updated successfully")
            break

    if not found:
        print("Problem not Found")
def statistics(problems):
    total = len(problems)
    easy = 0
    medium = 0
    hard = 0
    for problem in problems:
        if problem["difficulty"] == "easy":
            easy += 1
        elif  problem["difficulty"] == "medium" :
            medium += 1
        elif problem["difficulty"] == "hard" :
            hard += 1
    print("Total Problems Solved: ", total)        
    print("Easy Problems Solved: ", easy)
    print("Medium Problems Solved: ", medium)
    print("Hard Problems Solved: ", hard)
def get_difficulty_name(problem):
    difficulty_order = {"easy":1, "medium":2, "hard":3}
    return difficulty_order[problem["difficulty"]]
def sort_problems(problems):
    choice = int(input("Sort By:\n1)Problem Name or 2)Difficulty or 3)Topic or 4)Date\n"))
    if choice == 1:
        problems.sort(key = lambda problem: problem["problem_name"])
    elif choice == 2:
        problems.sort(key = get_difficulty_name)
    elif choice == 3:
        problems.sort(key = lambda problem:problem["topic"])
    elif choice == 4:
        problems.sort(key = lambda problem:problem["date"])
    else:
        print("Invalid Choice. Enter a Correct Choice. ")
    save_data(problems, DATA_FILE)
    view_problems(problems)
def get_topic():
    topic_name = input("Name of the Topic: ")
    topic_name = topic_name.lower()
    topic_name = topic_name.strip()
    return topic_name
def export_problems(problems):
    choice = int(input("***Export Problems***\n1)Export All\n2)Export by Difficulty\n3)Export by Topic\n4)Back\n"))
    if choice == 1:
        filename = "all_problems.json"
        save_data(problems, filename)
    elif choice == 2:
        difficulty_name = get_difficulty()
        filtered_problems = [
            problem
            for problem in problems
            if difficulty_name == problem["difficulty"]
        ]
        filename = difficulty_name + "_problems.json"
        save_data(filtered_problems, filename)
    elif choice == 3:
        topic_name = get_topic()
        filtered_problems = [
            problem
            for problem in problems
            if topic_name == problem["topic"]
        ]
        filename = topic_name + "_problems.json"
        save_data(filtered_problems, filename)

problems = load_data()
while True:
    print("**MENU**")
    try:
        choice = int(input("Enter your choice:\n1)Add a Problem or 2)View Problems or 3)Search Problems or 4)Delete Problem or 5)Edit a Problem or 6)Statistics or 7)Sort Problems or 8)Export Problems or 9)Exit\n"))
        if choice == 1:
            add_problem(problems)
            save_data(problems , DATA_FILE)
        elif choice == 2:
            view_problems(problems)
        elif choice == 3:
            search_problems(problems)
        elif choice == 4:
            delete_problem(problems)
        elif choice == 5:
            edit_problem(problems)
        elif choice == 6:
            statistics(problems)
        elif choice == 7:
            sort_problems(problems)
        elif choice == 8:
            export_problems(problems)
        elif choice == 9:
            break
        else:
            print("Invalid Choice")
    except ValueError:
        print("Enter only the Digits which are Specified")