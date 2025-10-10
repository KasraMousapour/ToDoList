class Project:
    names_list = []
    count = 0
    def __init__(self,name:str,description:str):
        if Project.count > MAX_NUMBER_OF_PROJECT:
            raise ValueError("The number of projects is full")
        elif name in Project.names_list:
            raise ValueError("The name is used")
        elif len(name.split()) > 50:
            raise ValueError("The name must be at least 50 words")
        elif len(description.split()) > 150:
            raise ValueError("The description must be at least 150 words")
        else:
            self.name = name
            self.description = description
            Project.names_list.append(name)
            count += 1

      




