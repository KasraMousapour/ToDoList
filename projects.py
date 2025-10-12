from tasks import Task
from collections.abc import Sequence
class Project:
    names_list = []
    count = 0
    _name:str
    _description:str
    _tasks:Sequence[Task]
    def __init__(self,name:str,description:str):
        if Project.count > MAX_NUMBER_OF_PROJECT:
            raise ValueError("The number of projects is full")
        else:
            self.name(name)
            self.description(description)
            Project.names_list.append(name)
            count += 1

    @property
    def name(self):
        return self._name   
    
    @property
    def description(self):
        return self._description
    
    @property
    def tasks(self):
        return self._tasks
    
    @name.setter
    def name(self, name:str):
        if name in Project.names_list:
            raise ValueError("The name is used")
        elif len(name.split()) > 50:
            raise ValueError("The name must be at least 50 words")
        else:
            self._name = name

    @description.setter
    def description(self, description:str):
        if len(description.split()) > 150:
            raise ValueError("The description must be at least 150 words")
        else:
            self._description = description

    @tasks.setter
    def tasks(self, tasks:Sequence[Task]):
        self._tasks = tasks

    def add_task(self, new_task:Task):
        try:
            self.tasks.append(new_task)  
        except:
            print("can't add")             

    def update_name(self,new_name:str):
        self.name(new_name)
        print("The name successfully updated.")

    def update_description(self, new_description:str):
        self.description(new_description)
        print("The description successfully updated.")

    def show_tasks(self):
        if self.tasks:
            for task in self.tasks:
                print(f"name:{task.name}, description:{task.description}, status:{task.status}, deadline:{task.deadline}")
        else:
            print("no task")        


    def delete_project(self):
        del self
        return "successfully deleted" 

       




      




