from typing import Literal
from datetime import datetime
class Task:
    names_list = []
    count = 0
    _name : str
    _description : str
    _status:Literal["done" ,"doing" ,"todo"]="todo"
    _deadline:str

    def __init__(self,name:str,description:str,status:Literal["done" ,"doing" ,"todo"]="todo",deadline:str=""):
        if Task.count > MAX_NUMBER_OF_TASK:
            raise ValueError("The number of tasks is full")
        else:
            self.name(name)
            self.description(description)
            self.status(status)
            self.deadline(deadline)
            Task.names_list.append(name)
            count += 1

    @property
    def name(self):
        return self._name
    
    @property
    def description(self):
        return self._description
    
    @property
    def status(self):
        return self._status
    
    @property
    def deadline(self):
        return self._deadline

    @name.setter
    def name(self, name:str):
        if not name:
            raise ValueError("Name cannot be empty.")
        elif name in Task.names_list:
            raise ValueError("The name is used")
        elif len(name.split()) > 30:
            raise ValueError("The name must be at least 30 words")
        else:
            self._name = name    

    @description.setter
    def description(self, description:str):
        if len(description.split()) > 150:
            raise ValueError("The description must be at least 150 words")
        else:
            self._description = description

    @status.setter
    def status(self, status:Literal["done" ,"doing" ,"todo"]="todo"):
        try:
            self._status = status
        except ValueError:
            print("The status must be in done or doing mode.")    

    @deadline.setter
    def deadline(self, deadline):
        if deadline:
            try:
                datetime.strptime(deadline, "%Y-%m-%d")
                self._deadline = deadline
            except ValueError:
                print("the deadline format must be YYYY-MM-DD")


    def update_status(self, new_status:Literal["done" , "doing"]):
        self.status = new_status
        print("successfully status changed.")

    def update_name(self, new_name):
        self.name(new_name)
    
        

        

