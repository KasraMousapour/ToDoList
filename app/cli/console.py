import argparse
from datetime import datetime
from db.session import SessionLocal
from services.project_services import ProjectService
from services.task_services import TaskService
from models.task import TaskStatus
from exceptions.service_exceptions import ValidationError, LimitExceededError, DeadlineError
from exceptions.repository_exceptions import DuplicateNameError


def list_projects(db):
    project_service = ProjectService(db)
    projects = project_service.project_repo.list()
    print("\n=== Projects ===")
    if not projects:
        print("No projects found.")
    else:
        for p in projects:
            print(f"{p.id}: {p.name}")
    return projects

def list_tasks(db, project_id):
    task_service = TaskService(db)
    tasks = task_service.task_repo.list_by_project(project_id)
    print(f"\n=== Tasks for Project {project_id} ===")
    for t in tasks:
        print(f"{t.id}: {t.name} (status={t.status}, deadline={t.deadline}, closed_at={t.closed_at})")
    return tasks

def add_project_and_tasks(db):
    project_service = ProjectService(db)
    task_service = TaskService(db)

    print("\n=== Add New Project ===")
    name = input("Project name: ")
    desc = input("Project description: ")

    try:
        project = project_service.create_project(name=name, description=desc)
        print(f"[OK] Project created: {project.name}")
    except (ValidationError, DuplicateNameError, LimitExceededError) as e:
        print(f"[ERROR] Project creation failed: {e}")
        return

    while True:
        print("\n=== Add Task ===")
        tname = input("Task name: ")
        tdesc = input("Task description: ")
        status_input = input("Task status (todo/doing/done) [default=todo]: ") or "todo"
        deadline_input = input("Deadline (YYYY-MM-DD) [optional]: ")

        deadline = None
        if deadline_input:
            try:
                deadline = datetime.strptime(deadline_input, "%Y-%m-%d")
            except ValueError:
                print("[ERROR] Invalid deadline format, skipping deadline.")

        try:
            task = task_service.create_task(
                project_id=project.id,
                name=tname,
                description=tdesc,
                status=TaskStatus[status_input],
                deadline=deadline
            )
            print(f"[OK] Task created: {task.name}")
        except (ValidationError, DuplicateNameError, LimitExceededError, DeadlineError) as e:
            print(f"[ERROR] Task creation failed: {e}")

        more = input("Add another task? (y/n): ").lower()
        if more != "y":
            break

def update_or_remove_project(db, project_id):
    project_service = ProjectService(db)
    task_service = TaskService(db)

    project = project_service.project_repo.get(project_id)
    if not project:
        print("Project not found.")
        return

    print(f"\nSelected Project: {project.name}")
    choice = input("Do you want to update (u) or remove (r) this project? ").lower()

    if choice == "u":
        new_name = input("New project name (leave blank to keep current): ")
        new_desc = input("New project description (leave blank to keep current): ")
        update_data = {}
        if new_name:
            update_data["name"] = new_name
        if new_desc:
            update_data["description"] = new_desc
        if update_data:
            try:
                project = project_service.update_project(project.id, **update_data)
                print(f"[OK] Project updated: {project.name}")
            except (ValidationError, DuplicateNameError) as e:
                print(f"[ERROR] Project update failed: {e}")

        # Update tasks
        tasks = list_tasks(db, project.id)
        if tasks:
            task_id = int(input("Enter task ID to update/remove: "))
            task = task_service.task_repo.get(task_id)
            if not task:
                print("Task not found.")
                return
            action = input("Update (u) or Remove (r) task? ").lower()
            if action == "u":
                new_name = input("New task name (leave blank to keep current): ")
                new_desc = input("New task description (leave blank to keep current): ")
                new_status = input("New status (todo/doing/done) [leave blank to keep current]: ")
                new_deadline = input("New deadline (YYYY-MM-DD) [leave blank to keep current]: ")

                update_data = {}
                if new_name:
                    update_data["name"] = new_name
                if new_desc:
                    update_data["description"] = new_desc
                if new_status:
                    update_data["status"] = TaskStatus[new_status]
                if new_deadline:
                    try:
                        update_data["deadline"] = datetime.strptime(new_deadline, "%Y-%m-%d")
                    except ValueError:
                        print("[ERROR] Invalid deadline format, skipping deadline.")

                try:
                    task = task_service.update_task(task.id, **update_data)
                    print(f"[OK] Task updated: {task.name}")
                except (ValidationError, DuplicateNameError, DeadlineError) as e:
                    print(f"[ERROR] Task update failed: {e}")
            elif action == "r":
                task_service.delete_task(task.id)
                print(f"[OK] Task {task_id} removed.")

    elif choice == "r":
        project_service.delete_project(project.id)
        print(f"[OK] Project {project_id} removed.")

def interactive_cli():
    db = SessionLocal()
    try:
        projects = list_projects(db)
        if not projects:
            print("\nNo projects found. Let's add a new one.")
            add_project_and_tasks(db)
        else:
            project_id = int(input("\nEnter project ID to manage or type 0 to add new: "))
            if project_id == 0:
                add_project_and_tasks(db)
            else:
                update_or_remove_project(db, project_id)
    finally:
        db.close()

def main():
    parser = argparse.ArgumentParser(description="Interactive CLI for projects and tasks")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    subparsers.add_parser("interactive", help="Run interactive mode to manage projects and tasks")

    args = parser.parse_args()

    if args.command == "interactive":
        interactive_cli()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()

