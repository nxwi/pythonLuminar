# Create a program that generates a simple to-do list.

to_do_list = []
while True:
    task = input("Enter a task (enter 'done' to finish): ")
    if task == "done":
        break
    else:
        to_do_list.append(task)

print("To-do list:")
for task in to_do_list:
    print("-", task)
