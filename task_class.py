"""Task and TodoList classes for task management"""
import json
from datetime import datetime

class Task:
    """Represents a single task with priority and due date"""
    
    def __init__(self, description, priority, due_date, status="Pending"):
        self.description = description
        self.priority = priority  # High, Medium, Low
        self.due_date = due_date  # YYYY-MM-DD
        self.status = status  # Pending, Completed
        self.created_date = datetime.now().strftime("%Y-%m-%d")
    
    def mark_complete(self):
        """Mark task as completed"""
        self.status = "Completed"
    
    def to_dict(self):
        """Convert task to dictionary for JSON storage"""
        return {
            "description": self.description,
            "priority": self.priority,
            "due_date": self.due_date,
            "status": self.status,
            "created_date": self.created_date
        }
    
    def __str__(self):
        return f"[{self.priority}] {self.description} (Due: {self.due_date}) - {self.status}"


class TodoList:
    """Manages collection of tasks"""
    
    def __init__(self, filename="todo.json"):
        self.tasks = []
        self.filename = filename
        self.load_tasks()
    
    def add_task(self, description, priority, due_date):
        """Add new task to list"""
        task = Task(description, priority, due_date)
        self.tasks.append(task)
        self.save_tasks()
        return f"✓ Task added: {description}"
    
    def mark_task_complete(self, task_index):
        """Mark specific task as completed"""
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].mark_complete()
            self.save_tasks()
            return f"✓ Task marked complete: {self.tasks[task_index].description}"
        return "✗ Invalid task number"
    
    def delete_task(self, task_index):
        """Delete task from list"""
        if 0 <= task_index < len(self.tasks):
            removed = self.tasks.pop(task_index)
            self.save_tasks()
            return f"✓ Task deleted: {removed.description}"
        return "✗ Invalid task number"
    
    def save_tasks(self):
        """Save tasks to JSON file"""
        try:
            with open(self.filename, 'w') as f:
                json.dump([task.to_dict() for task in self.tasks], f, indent=2)
        except Exception as e:
            print(f"Error saving tasks: {e}")
    
    def load_tasks(self):
        """Load tasks from JSON file"""
        try:
            with open(self.filename, 'r') as f:
                data = json.load(f)
                self.tasks = [Task(t['description'], t['priority'], 
                             t['due_date'], t['status']) for t in data]
        except FileNotFoundError:
            self.tasks = []
        except Exception as e:
            print(f"Error loading tasks: {e}")
            self.tasks = []
    
    def get_statistics(self):
        """Get task statistics"""
        stats = {
            'total': len(self.tasks),
            'pending': len([t for t in self.tasks if t.status == "Pending"]),
            'completed': len([t for t in self.tasks if t.status == "Completed"]),
            'high': len([t for t in self.tasks if t.priority == "High"]),
            'medium': len([t for t in self.tasks if t.priority == "Medium"]),
            'low': len([t for t in self.tasks if t.priority == "Low"])
        }
        return stats
