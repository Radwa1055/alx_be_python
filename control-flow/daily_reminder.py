task = input ("inter your task")
priority = input ("priority (high/medium/low)").lower()
time_bound = input("Is the task is time-bound? (yes or no)").lower()
match priority:
    case "high":
        reminder = task + " is a high priority task."
    case "medium":
        reminder = task + " is a medium priority task."
    case "low":
        reminder = task + " is a low priority task."
    case _:
        reminder = task + " has an unknown priority level."

if time_bound == "yes":
    reminder = reminder + " It requires immediate attention today!"
else:
    reminder = "Note: " + reminder + " Consider completing it when you have free time."
print("\nReminder:", reminder)


