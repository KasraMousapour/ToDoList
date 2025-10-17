from typing import Literal
from datetime import datetime
from dotenv import load_dotenv
import os

# load_dotenv()

class Task:
    names_list = []
    count = 0
    _name : str
    _description : str
    _status:Literal["done" ,"doing" ,"todo"]="todo"
    _deadline:str
    # max_number = os.getenv("MAX_NUMBER_OF_TASK")
    MAX_NUMBER_OF_TASK = 50

    def __init__(self,name:str,description:str="",status:Literal["done" ,"doing" ,"todo"]="todo",deadline:str=""):
        if Task.count > Task.MAX_NUMBER_OF_TASK:
            raise ValueError("The number of tasks is full")
        elif name in Task.names_list:
            raise ValueError("The name is used")
        elif len(name.split()) > 30:
            raise ValueError("The name must be at least 30 words")
        elif len(description.split()) > 150:
            raise ValueError("The description must be at least 150 words")
        elif deadline:
            try:
                datetime.strptime(deadline, "%Y-%m-%d")    
            except ValueError:
                print("the deadline format must be YYYY-MM-DD")
    
        self._name = name
        self._description = description
        self._status = status
        self._deadline = deadline
        Task.names_list.append(name)
        Task.count += 1

    def delete_task(self):
        Task.count -= 1
        del self
        print("successfully deleted!!")    

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

    def update_name(self, new_name):
        self.name(new_name)
        return f"The name updated to {new_name}"

    def update_description(self, new_description):
        self.name(new_description)
        return f"The description updated to {new_description}"

    def update_status(self, new_status:Literal["done" , "doing"]):
        self.status(new_status)
        return f"The status updated to {new_status}"

    def update_deadline(self, new_deadline):
        self.deadline(new_deadline)
        return f"The deadline updated to {new_deadline}"
    
    def delete_task(self):
        try:
            del self
            return "seccessfully deleted"
        except:
            return "something is wrong"

        



        

