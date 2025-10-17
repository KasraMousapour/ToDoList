# from tasks import Task
# from projects import Project

# p1 = Project("portfolio","lorem ipsome")
# p1.update_name("web design") 
# t1 = Task("html","","done","1955-11-05")
# t2 = Task("css","styling", "todo", "2025-12-04")
# # p1.add_task(t1)
# # p1.add_task(t2)
# # print(p1.delete_project())
# temp = 0
# try:
#     t1.name = ""
# except ValueError as e:
#     print(e)
# else:
#     temp = 1       
# print(temp)    

class Item:
    def __init__(self, name):
        self.name = name
        print(f"Item '{self.name}' created.")

    def delete_item(self):
        del self
        print(f"Item successfully  deleted.")

class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, name):
        item = Item(name)
        self.items.append(item)

    def delete_item(self, name):
        for item in self.items:
            if item.name == name:
                self.items.remove(item)
                item.delete_item()  # triggers __del__ if no other references
                print(f"Item '{name}' deleted.")
                return
        print(f"Item '{name}' not found.")

    def show_items(self):
        print("Current items:")
        for item in self.items:
            print(f"- {item.name}")

# Example usage
inv = Inventory()
inv.add_item("Book")
inv.add_item("Pen")
inv.show_items()

inv.delete_item("Pen")
inv.show_items()
