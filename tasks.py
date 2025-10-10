from typing import Literal
class Task:
    names_list = []
    count = 0
    def __init__(self,name:str,description:str,status:Literal["done" ,"doing" ,"todo"]="todo"):
        if Task.count > MAX_NUMBER_OF_TASK:
            raise ValueError("The number of tasks is full")
        elif name in Task.names_list:
            raise ValueError("The name is used")
        elif len(name.split()) > 30:
            raise ValueError("The name must be at least 30 words")
        elif len(description.split()) > 150:
            raise ValueError("The description must be at least 150 words")
        else:
            self.name = name
            self.description = description
            self.status = status
            Task.names_list.append(name)
            count += 1
