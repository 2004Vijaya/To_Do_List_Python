tasks=[]

#the addTask function is used to add the elements in to list.

def addTask():  # add task is a name of the function.
    task=int(input("Please enter the number of tasks:"))
    for i in range(task):#loop iterates until number of tasks are entered in to list.
        task=input("Enter the task:")
        tasks.append(task)#the entered tasks are appended to the empty lis tasks[].
        print("The task {} added to the list".format(tasks))#the added items to the list will be displayes on console.


#this task is used to display the added tasks in to the list.

def listTasks():
    if not tasks:#if there are no tasks are present in the list then the below statement will be executed .
        print("There are no tasks are present in the list..")
    else:
        print("Present Tasks are.")
        print("------------------")
        for index, task in enumerate(tasks):#enumerate method is to calculate the index of the tasks.
            print(f"Task {index}. {task}")
        

def deleteTask():
    listTasks()
    try:
        tasktodelete=int(input("Enter the task to delete:"))
        if tasktodelete<len(tasks):
            tasks.pop(tasktodelete)
            print("The task {} has been  removed..".format(tasktodelete))
            print("Present Tasks are.")
            print("------------------")
            for index, task in enumerate(tasks):
                print(f"Task {index}. {task}")

        else:
            print("The task {} was not found".format(tasktodelete))
    except:
        print("Invalid input..")
    


print("welcome to the TO DO LIST APP...")
print("---------------------------------")
while True:
    print("\n")
    print("Please choose one of the following options")
    print("------------------------------------------")
    print("1.Add a new task")
    print("2.Delete a Task")
    print("3.List Tasks")
    print("4.Quit from app")

    choice=input("enter your choice:")
    if(choice=="1"):
        addTask()
    elif(choice=="2"):
        deleteTask()
    elif(choice=="3"):
        listTasks()
    elif(choice=="4"):
        break
    else:
        print("Invalid input...")

print("Good BYeee......")     
