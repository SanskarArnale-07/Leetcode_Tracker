import json
import os
DATA_FILE = os.path.join(os.path.dirname(__file__),"data.json")
print("Main.py Location", os.path.dirname(os.path.abspath(__file__)))
problems = []
def add_problem(problems):
#Storing all this in dictionary and dictionaries into list
    problem_name=input("Enter the Name of the Problem: ")
    difficulty= get_difficulty()
    topic= get_topic()
    date = input("Enter the Date you Solved the Problem: ")
    problem_overview = {"problem_name" : problem_name, "difficulty": difficulty, "topic":topic, "date":date}
    print("=" * 40)
    print("✅ Problem Added Successfully!")
    print("=" * 40)
    problems.append(problem_overview)
def get_difficulty():
    while True:
        difficulty = input("Enter the Difficulty of the Problem: ")
        difficulty = difficulty.lower()
        if difficulty in ["easy", "medium", "hard"]:
            return difficulty
        print("Invalid Difficulty. Please Enter Easy, Medium or Hard.")
def view_problems(problems):
    if not problems:
        print("No Problems Found.")
        return
    for index , problem in enumerate(problems,start=1):
        print("-" * 40)
        print(f"Problem #{index}")
        print()
        print(f"Name       : {problem['problem_name']}")
        print(f"Difficulty : {problem['difficulty'].capitalize()}")
        print(f"Topic      : {problem['topic'].capitalize()}")
        print(f"Date       : {problem['date']}")
        print("-" * 40)
def save_data(problems , filename):
    with open(filename, "w") as f:
        json.dump(problems,f, indent = 4)
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
        choice = int(input("Enter your choice:\n1)Problem Name\n2)Difficulty\n3)Topic\n"))
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
            topic_name= get_topic()
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
    print("-" * 40)
    print()
    print(f"Name       : {problem['problem_name']}")
    print(f"Difficulty : {problem['difficulty'].capitalize()}")
    print(f"Topic      : {problem['topic'].capitalize()}")
    print(f"Date       : {problem['date']}")
    print("-" * 40)
def delete_problem(problems):
    problem_name = input("Enter the Name of the Problem: ")
    found = False
    for problem in problems:
        if problem_name == problem["problem_name"]:
            problems.remove(problem)    #From the Problems list remove the xyz problem dictionary
            print("=" * 40)
            print("✅ Problem Deleted Successfully!")
            print("=" * 40)
            found = True
            save_data(problems, DATA_FILE)
            print("Goodbye! 👋")
            break
    if not found:
        print("Problem Does not Exist")
def edit_problem(problems):
    problem_name = input("Enter the Name of the Problem: ")
    found = False
    for problem in problems:
        if problem_name == problem["problem_name"]:
            found = True
            choice = int(input("Enter your choice:\n1)Name:\n2)Difficulty\n3)Topic\n4)Date\n"))
            if choice == 1:
                name = input("Enter the Updated Name of the Problem: ")
                problem["problem_name"] = name
            elif choice == 2:
                difficulty = input("Enter the Updated Difficulty of the Problem: ")
                problem["difficulty"] = difficulty
            elif choice == 3:
                topic = get(topic)
                problem["topic"] = topic
            elif choice == 4:
                date = input("Enter the Updated Date of the Problem: ")
                problem["date"] = date
            save_data(problems, DATA_FILE)
            print("Problem updated successfully")
            print("Goodbye! 👋")
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
    print("========== Statistics ==========")
    print("Total  :", total)        
    print("Easy   :", easy)
    print("Medium :", medium)
    print("Hard   :", hard)
    print("================================")
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
    print("Problems Sorted Successfully")
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
        print("=" * 40)
        print(f"✅ Exported {len(problems)} problems.")
        print(f"📄 Saved to: {filename}")
        print("=" * 40)
    elif choice == 2:
        difficulty_name = get_difficulty()
        filtered_problems = [
            problem
            for problem in problems
            if difficulty_name == problem["difficulty"]
        ]
        filename = difficulty_name + "_problems.json"
        save_data(filtered_problems, filename)
        print("=" * 40)
        print(f"✅ Exported {len(filtered_problems)} problems.")
        print(f"📄 Saved to: {filename}")
        print("=" * 40)
    elif choice == 3:
        topic_name = get_topic()
        filtered_problems = [
            problem
            for problem in problems
            if topic_name == problem["topic"]
        ]
        filename = topic_name + "_problems.json"
        save_data(filtered_problems, filename)
        print("=" * 40)
        print(f"✅ Exported {len(filtered_problems)} problems.")
        print(f"📄 Saved to: {filename}")
        print("=" * 40)
    

problems = load_data()
while True:
    print("=" * 50)
    print("      LEETCODE TRACKER")
    print("=" * 50)
    try:
        choice = int(input("Enter your choice:\n"
        "1)Add Problems\n"
        "2)View Problems\n"
        "3)Search Problems\n"
        "4)Delete Problems\n"
        "5)Edit Problems\n"
        "6)Statistics\n"
        "7)Sort Problems\n"
        "8)Export Problems\n"
        "9)Exit\n"))
        print("=" * 50)
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