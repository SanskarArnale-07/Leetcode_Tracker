import json
problems = []
def Add_Problem():
#Storing all this in dictionary and dictionaries into list
    problem_name=input("Enter the Name of the Problem: ")
    difficulty= input("Enter the Difficulty of the Problem: ")
    topic= input("Enter the Topic of the Problem: ")
    date = input("Enter the Date you Solved the Problem: ")
    problem_overview = {"problem_name" : problem_name, "difficulty": difficulty, "topic":topic, "date":date}
    print(problem_overview)
    problems.append(problem_overview)
def View_Problems():
    for problem in problems:
        print(problem)
with open("data.json", "r") as f:
    problems = json.load(f)
while True:
    print("**MENU**")
    choice = int(input("Enter your choice:\n1)Add a Problem:\n2)View Problems\n3)Exit:\n"))
    if choice == 1:
        Add_Problem()
        with open("data.json", "w") as f:
            json.dump(problems, f)
    elif choice == 3:
        break
    elif choice == 2:
        View_Problems()
    else:
        print("Invalid Choice")
