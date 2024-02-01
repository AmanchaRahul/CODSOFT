#TASK-1
#TO-DO-LIST

todolist='''
1.Add task
2.Delete task
3.Show all tasks
4.Exit'''

tasks=[]

def add_task():
    task=input("enter the task: ")
    tasks.append(task)
    print("your task is been added successfully!")
    print()
    
def delete_task():
    task_num=int(input("enter the task number, you want to delete: "))
    if 1 <= task_num <= len(tasks):
        tasks.pop(task_num - 1)  # Adjust index to start from 1
        print("selected task is successfully deleted!")
    else:
        print("Invalid task number. Please try again.")
    
def show_tasks():

    print("######TASKS######")
    if tasks:
     for taskindex, task in enumerate(tasks, start=1):
        print(f"{taskindex}. {task}")
     print()
    else:
        print("no task is there!")
        
while True:
    print("======TO DO LIST======")
    print(todolist)
    choice=int(input("select any choice from the above: "))
    print()

    if choice==1:
       add_task()
    elif choice==2:
       delete_task()
    elif choice==3:
       show_tasks()
    elif choice==4:
        print("you ended your tasks!")
        break
    else:
        print("Invalid choice")



