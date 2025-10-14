from project_manager import ProjectManager
from projects import Project
from tasks import Task

def main():
    manager = ProjectManager()
    while True:
        print("\n📁 Project Manager")
        print("1. Add project")
        print("2. Rename project")
        print("3. change project description ")
        print("4. delete project")
        print("5. task management of project")
        print("6. Show all projects")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter project name: ")
            manager.add_project(name)

        elif choice == "2":
            old_name = input("Enter current project name: ")
            new_name = input("Enter new project name: ")
            manager.rename_project(old_name, new_name)

        elif choice == "3":
            name = input("Enter project name: ") 
            new_description = input("Enter new description: ")  
            manager.change_description(name,new_description) 

        elif choice == "4":
            name = input("Enter project name: ")
            manager.delete_project(name)

        elif choice == "5":
            name = input("Enter project name: ")
            project = manager.find_project(name)
            while True:
                print(f"task management of {name} project:")
                print("1. Add task ")
                print("2. rename task ")
                print("3. change task description ")
                print("4. change task status ")
                print("5. delete task ")
                print("6. show all tasks of project ")
                print("7. back ")

                choice2 = input("Choose an option: ")

                if choice2 == "1":
                    task = Task()
                    temp = 1
                    while temp == 1 :
                        name = input("Enter task name: ")
                        try:
                            task.name = name
                        except ValueError as e:
                            print(e)
                        else:
                            temp = 0    
                    temp = 1
                    while temp == 1 :
                        description = input("Enter task description: ")
                        try:
                            task.description = description
                        except ValueError as e:
                            print(e)
                        else:
                            temp = 0 
                    temp = 1
                    while temp == 1 :
                        deadline = input("Enter task deadline(YYYY-MM-DD): ")
                        try:
                            task.deadline = deadline
                        except ValueError as e:
                            print(e)
                        else:
                            temp = 0 
                    project.add_task(task) 
                    print("The task successfully added. ")      

                elif choice2 == "2":
                    name = input("Enter task name: ")
                    task = project.find_task(name)     
                    if task:
                        temp = 1
                        while temp == 1 :
                            new_name = input("Enter new name: ")
                            try:
                                task.name = new_name
                            except ValueError as e:
                                print(e)
                            else:
                                temp = 0  
                        print("The task successfully renamed. ")  
                    else:
                        print("task not found!")     

                elif choice2 == "3":
                    name = input("Enter task name: ")
                    task = project.find_task(name)     
                    if task:
                        temp = 1
                        while temp == 1 :
                            new_description = input("Enter new description: ")
                            try:
                                task.description = new_description
                            except ValueError as e:
                                print(e)
                            else:
                                temp = 0  
                        print("The task description successfully changed. ")  
                    else:
                        print("task not found!") 

                elif choice2 == "4":
                    name = input("Enter task name: ")
                    task = project.find_task(name)     
                    if task:
                        temp = 1
                        while temp == 1 :
                            new_status = input("Enter new status(1: doing , 2: done): ")
                            try:
                                if new_status == "1":
                                    task.status = "doing"
                                elif new_status == "2":
                                    task.status = "done"
                                else:
                                    raise ValueError("Please enter between 1 or 2.")        

                            except ValueError as e:
                                print(e)
                            else:
                                temp = 0  
                        print("The task status successfully changed. ")  
                    else:
                        print("task not found!") 

                elif choice2 == "5":
                    name = input("Enter task name: ")
                    task = project.find_task(name) 
                    if task:
                        del task
                    else:
                        print("task not found!")

                elif choice2 == "6":
                    project.show_tasks()

                elif choice2 == "7":
                    break        

        elif choice == "6":
            manager.show_projects()

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()