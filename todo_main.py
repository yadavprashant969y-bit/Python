"""Main To-Do List Application"""
from task_class import TodoList
from sorter import TaskSorter
from visualization import plot_statistics
import sys

def display_menu():
    """Display main menu"""
    print("\n" + "="*50)
    print("📋 TO-DO LIST MANAGER")
    print("="*50)
    print("1. Add New Task")
    print("2. View All Tasks (by Priority)")
    print("3. View Tasks (by Due Date)")
    print("4. Filter Pending Tasks")
    print("5. Filter Completed Tasks")
    print("6. Mark Task Complete")
    print("7. Delete Task")
    print("8. View Statistics")
    print("9. Visualize Statistics")
    print("10. Exit")
    print("="*50)

def add_task(todo_list):
    """Add new task"""
    print("\n--- ADD NEW TASK ---")
    description = input("Task: ").strip()
    
    print("Priority (High/Medium/Low): ", end="")
    priority = input().strip().capitalize()
    if priority not in ["High", "Medium", "Low"]:
        print("✗ Invalid priority! Set to Medium.")
        priority = "Medium"
    
    due_date = input("Due Date (YYYY-MM-DD): ").strip()
    
    result = todo_list.add_task(description, priority, due_date)
    print(result)

def view_tasks(todo_list, sort_type="priority"):
    """View tasks with sorting"""
    if not todo_list.tasks:
        print("\n✗ No tasks yet!")
        return
    
    sorted_tasks = TaskSorter.display_sorted_list(todo_list.tasks, sort_type)
    sort_label = "Priority" if sort_type == "priority" else "Due Date"
    
    print(f"\n TASK LIST (Sorted by {sort_label}):")
    print("-" * 50)
    for idx, task in enumerate(sorted_tasks, 1):
        status_icon = "✓" if task.status == "Completed" else "○"
        print(f"{idx}. {status_icon} [{task.priority}] {task.description}")
        print(f"   Due: {task.due_date} | Status: {task.status}\n")

def filter_tasks(todo_list, status):
    """Filter and display tasks by status"""
    filtered = TaskSorter.filter_by_status(todo_list.tasks, status)
    
    if not filtered:
        print(f"\n✗ No {status} tasks!")
        return
    
    print(f"\n🔍 {status.upper()} TASKS:")
    print("-" * 50)
    for idx, task in enumerate(filtered, 1):
        print(f"{idx}. [{task.priority}] {task.description}")
        print(f"   Due: {task.due_date}\n")

def mark_complete(todo_list):
    """Mark task as completed"""
    if not todo_list.tasks:
        print("\n✗ No tasks!")
        return
    
    view_tasks(todo_list, "priority")
    try:
        task_num = int(input("Enter task number to complete: "))
        # Find task in original list
        sorted_tasks = TaskSorter.display_sorted_list(todo_list.tasks, "priority")
        task_to_complete = sorted_tasks[task_num - 1]
        original_index = todo_list.tasks.index(task_to_complete)
        
        result = todo_list.mark_task_complete(original_index)
        print(result)
    except (ValueError, IndexError):
        print("✗ Invalid task number!")

def delete_task(todo_list):
    """Delete task"""
    if not todo_list.tasks:
        print("\n✗ No tasks!")
        return
    
    view_tasks(todo_list, "priority")
    try:
        task_num = int(input("Enter task number to delete: "))
        sorted_tasks = TaskSorter.display_sorted_list(todo_list.tasks, "priority")
        task_to_delete = sorted_tasks[task_num - 1]
        original_index = todo_list.tasks.index(task_to_delete)
        
        result = todo_list.delete_task(original_index)
        print(result)
    except (ValueError, IndexError):
        print("✗ Invalid task number!")

def show_statistics(todo_list):
    """Display task statistics"""
    stats = todo_list.get_statistics()
    
    print("\n📊 TASK STATISTICS:")
    print("-" * 50)
    print(f"Total Tasks: {stats['total']}")
    print(f"Pending: {stats['pending']}")
    print(f"Completed: {stats['completed']}")
    print("-" * 50)
    print(f"High Priority: {stats['high']}")
    print(f"Medium Priority: {stats['medium']}")
    print(f"Low Priority: {stats['low']}")
    print("-" * 50)

def task_count_decorator(func):
    """Decorator to display task count"""
    def wrapper(todo_list):
        stats = todo_list.get_statistics()
        print(f"\n✓ Loaded {stats['total']} tasks ({stats['pending']} pending)")
        return func(todo_list)
    return wrapper

@task_count_decorator
def startup_message(todo_list):
    """Startup message with task count"""
    pass

def main():
    """Main application loop"""
    todo_list = TodoList("todo.json")
    startup_message(todo_list)
    
    while True:
        display_menu()
        choice = input("Select option: ").strip()
        
        if choice == "1":
            add_task(todo_list)
        elif choice == "2":
            view_tasks(todo_list, "priority")
        elif choice == "3":
            view_tasks(todo_list, "date")
        elif choice == "4":
            filter_tasks(todo_list, "Pending")
        elif choice == "5":
            filter_tasks(todo_list, "Completed")
        elif choice == "6":
            mark_complete(todo_list)
        elif choice == "7":
            delete_task(todo_list)
        elif choice == "8":
            show_statistics(todo_list)
        elif choice == "9":
            plot_statistics(todo_list)
        elif choice == "10":
            print("\n👋 Goodbye!")
            sys.exit()
        else:
            print("✗ Invalid option!")

if __name__ == "__main__":
    main()
