import json
problems = []
def add_problem(problems):
#Storing all this in dictionary and dictionaries into list
    problem_name=input("Enter the Name of the Problem: ")
    difficulty= input("Enter the Difficulty of the Problem: ")
    topic= input("Enter the Topic of the Problem: ")
    date = input("Enter the Date you Solved the Problem: ")
    problem_overview = {"problem_name" : problem_name, "difficulty": difficulty, "topic":topic, "date":date}
    print(problem_overview)
    problems.append(problem_overview)
def view_problems(problems):
    for problem in problems:
        print(problem)
def save_data(problems):
    with open("data.json", "w") as f:
        json.dump(problems,f)
def load_data():
    try:
        with open("data.json", "r") as f:
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
            save_data(problems)
            break
    if not found:
        print("Problem Does not Exist")
                      
problems = load_data()
while True:
    print("**MENU**")
    try:
        choice = int(input("Enter your choice:\n1)Add a Problem:\n2)View Problems:\n3)Exit:\n4)Search Problems:\n5)Delete Problem:"))
        if choice == 1:
            add_problem(problems)
            save_data(problems)
        elif choice == 3:
            break
        elif choice == 2:
            view_problems(problems)
        elif choice == 4:
            search_problems(problems)
        elif choice == 5:
            delete_problem(problems)
        else:
            print("Invalid Choice")
    except ValueError:
        print("Enter only the Digits which are Specified")