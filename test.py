from tasks import Task
from projects import Project

p1 = Project("portfolio","lorem ipsome")
p1.update_name("web design") 
t1 = Task("html","","done","1955-11-05")
p1.add_task(t1)
p1.show_tasks()