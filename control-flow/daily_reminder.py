task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a high priority task. Consider completing it soon.")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a medium priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a medium priority task. Plan to complete it when possible.")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a low priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a low priority task. Complete it at your convenience.")
    case _:
        print("Invalid priority entered. Please use 'high', 'medium', or 'low'.")


""" task = input("Enter your task:") 
priority = input("Priority (high/medium/low):")
time_bound = input("Is it time-bound? (yes/no):")

match priority:
    case "high":
        if time_bound == "yes":
            print(f"'{task}' is a {priority} priority task that requires immediate attention today!") 
        elif time_bound == "no":
            print(f"'{task}' is a {priority} priority task, Consider completing it when you have free time.")
    case "medium":
        if time_bound == "yes":
            print(f"'{task}' is a {priority} priority task that requires immediate attention today!") 
        elif time_bound == "no":
            print(f"'{task}' is a {priority} priority task, Consider completing it when you have free time.")
    case "low":
        if time_bound == "yes":
            print(f"'{task}' is a {priority} priority task that requires immediate attention today!") 
        elif time_bound == "no":
            print(f"'{task}' is a {priority} priority task, Consider completing it when you have free time.") """