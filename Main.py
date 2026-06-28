problems = []
#Storing all this in dictionary and dictionaries into list
problem_name=input("Enter the Name of the Problem: ")
difficulty= input("Enter the Difficulty of the Problem: ")
topic= input("Enter the Topic of the Problem: ")
date = input("Enter the Date you Solved the Problem: ")
problem_overview = {"problem_name" : problem_name, "difficulty": difficulty, "topic":topic, "date":date}
print(problem_overview)