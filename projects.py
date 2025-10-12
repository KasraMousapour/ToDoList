class Project:
    names_list = []
    count = 0
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

    def update_name(self,new_name:str):
        self.name(new_name)
        print("The name successfully updated.")

    def update_description(self, new_description:str):
        self.description(new_description)
        print("The description successfully updated.")


      




