# Todo Project
# CRUD => Create, Read, Update, Delete
# Name: Jagdish Parthsarthi Babalsure

import mysql.connector as mysql

con = mysql.connect(host="localhost", user="root", passwd="Shrud@3174")

cursor = con.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS TODO_APP")

print("Database initialized...")

cursor.execute("USE TODO_APP")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INT AUTO_INCREMENT PRIMARY KEY,
        description VARCHAR(50) NOT NULL,
        status ENUM('pending', 'completed') DEFAULT 'pending'
    )
""")

print("Table setup complete...")

def insert_task():
    task_desc = input("Enter task description: ")
    cursor.execute("INSERT INTO tasks (description) VALUES (%s)", (task_desc,))
    con.commit()
    print("-> Task successfully added!")

def list_tasks():
    cursor.execute("SELECT * FROM tasks")
    all_tasks = cursor.fetchall()
    if not all_tasks:
        print("No tasks available.")
    else:
        print("\nTask List:")
        for task in all_tasks:
            print(f"[ID: {task[0]}, Description: {task[1]}, Status: {task[2]}]")

def modify_task():
    list_tasks()
    task_id = input("Enter the ID of the task to modify: ")
    updated_task = input("Enter updated task description: ")
    cursor.execute("UPDATE tasks SET description = %s WHERE id = %s", (updated_task, task_id))
    con.commit()
    print("-> Task successfully updated!")

def complete_task():
    list_tasks()
    task_id = input("Enter the ID of the task to mark as completed: ")
    cursor.execute("UPDATE tasks SET status = 'completed' WHERE id = %s", (task_id,))
    con.commit()
    print("-> Task marked as completed!")

def remove_task():
    list_tasks()
    task_id = input("Enter the ID of the task to delete: ")
    cursor.execute("DELETE FROM tasks WHERE id = %s", (task_id,))
    con.commit()
    print("-> Task successfully deleted!")

while True:
    print("\nTask Manager")
    print("1) Add Task")
    print("2) View Tasks")
    print("3) Update Task")
    print("4) Mark as Completed")
    print("5) Delete Task")
    print("6) Exit")

    user_choice = input("Select an option: ")

    if user_choice == "1":
        insert_task()
    elif user_choice == "2":
        list_tasks()
    elif user_choice == "3":
        modify_task()
    elif user_choice == "4":
        complete_task()
    elif user_choice == "5":
        remove_task()
    elif user_choice == "6":
        print("Exiting Task Manager...")
        break
    else:
        print("Invalid selection, please try again!")

cursor.close()
con.close()
